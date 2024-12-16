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
        record_type = cleaned_data.get('record_type')
        access_type = cleaned_data.get('access_type')

        # Validar duplicados
        if Attendance.objects.filter(
            user=user,
            record_type=record_type,
            access_type=access_type,
            created_at__date=today
        ).exists():
            raise ValidationError("Ya existe un registro con este tipo y acceso para hoy.")
        
        return cleaned_data