from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    dni = models.CharField(max_length=255, unique=True, verbose_name='DNI')
    corporate_email = models.EmailField(blank=True, null=True, verbose_name='Correo corporativo')
    corporate_phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Teléfono corporativo')
    corporate_device_imei = models.CharField(max_length=255, blank=True, null=True, verbose_name='IMEI teléfono corporativo')
    employment_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Inicio de empleo')
    employment_end_date = models.DateTimeField(blank=True, null=True, verbose_name='Fin de empleo')
    #address = models.ForeignKey('locations.Address', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Dirección')
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Coordinador')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creación de registro')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
