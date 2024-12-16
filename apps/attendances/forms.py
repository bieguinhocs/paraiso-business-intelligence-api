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

        # Validar duplicados
        if Attendance.objects.filter(
            user=user,
            access_type=access_type,
            record_type=record_type,         
            created_at__date=today
        ).exists():
            raise ValidationError(f"Ya existe un registro de {access_type} de {record_type}!")

        # Recuperar las marcaciones existentes del usuario para el día actual
        user_attendances = Attendance.objects.filter(
            user=user,
            created_at__date=today
        ).order_by('created_at')

        # Validar que el primer registro del día sea "Jornada - Inicio"
        if not user_attendances.exists() and (access_type.name != 'Inicio' or record_type.name != 'Jornada'):
            raise ValidationError("El primer registro del día debe ser Inicio Jornada")

        return cleaned_data