from django import forms
from .models import Attendance
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'photo' in self.fields:
            self.fields['photo'].widget.attrs.update({
                'accept': 'image/*',
                'capture': 'camera',
            })

    def clean(self):
        cleaned_data = super().clean()

        # Obtener el usuario de la sesión
        user = self.request.user if self.request else None
        if not user:
            raise ValidationError("No se pudo determinar el usuario actual.")

        # Acceder a datos de la asistencia
        today = now().date()
        access_type = cleaned_data.get('access_type')
        record_type = cleaned_data.get('record_type')
        store = cleaned_data.get('store')

        # Validar duplicados
        if Attendance.objects.filter(
            user=user,
            access_type=access_type,
            record_type=record_type,         
            created_at__date=today
        ).exists():
            raise ValidationError(f"Ya existe un registro de {access_type} de {record_type}.")

        # Recuperar las marcaciones existentes del usuario para el día actual
        user_attendances = Attendance.objects.filter(
            user=user,
            created_at__date=today
        ).order_by('created_at')

        # Validar que las marcaciones estén completas
        if user_attendances.filter(access_type__name='Fin', record_type__name='Asistencia').exists():
            raise ValidationError("Las marcaciones para este día ya están completas. No puedes registrar más.")
        
        # Extraer las marcaciones actuales
        current_order = [
            (attendance.access_type.name, attendance.record_type.name)
            for attendance in user_attendances
        ]

        # Añadir la nueva marcación al orden
        current_order.append((access_type.name, record_type.name))

        # Validar el orden
        expected_order = [
            ('Inicio', 'Asistencia'),
            ('Inicio', 'Refrigerio'),
            ('Fin', 'Refrigerio'),
            ('Fin', 'Asistencia')
        ]

        # Validar que el primer registro del día sea "Inicio Asistencia"
        if not user_attendances.exists() and (access_type.name != 'Inicio' or record_type.name != 'Asistencia'):
            raise ValidationError("El primer registro del día debe ser Inicio de Asistencia.")

        # Validar si el usuario intenta registrar "Fin Asistencia" directamente después de "Inicio Asistencia"
        if len(current_order) == 2 and current_order == [
            ('Inicio', 'Asistencia'),
            ('Fin', 'Asistencia')
        ]:
            return cleaned_data  # Caso permitido, no es necesario validar más

        # Validar el orden de las marcaciones
        for i in range(len(current_order)):
            valid_order = expected_order[:i + 1]
            if current_order[:i + 1] != valid_order:
                missing_access_type, missing_record_type = expected_order[len(current_order[:i])]
                raise ValidationError(
                    f"No puedes registrar {access_type.name} de {record_type.name} porque falta la marcación de {missing_access_type} de {missing_record_type}."
                )

        return cleaned_data