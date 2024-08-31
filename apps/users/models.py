from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    dni = models.CharField(_('DNI'), max_length=255, unique=True)
    corporate_phone = models.CharField(_('corporate phone number'), max_length=255, blank=True, null=True)
    corporate_device_imei = models.CharField(_('corporate device imei'), max_length=255, blank=True, null=True)
    employment_start_date = models.DateTimeField(_('employment start'), blank=True, null=True)
    employment_end_date = models.DateTimeField(_('employment end'), blank=True, null=True)
    #address = models.ForeignKey('locations.Address', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Dirección')
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('coordinator'))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    # Campo de AbstractUser omitido y reemplazado por 'created_at'
    date_joined = models.DateTimeField(null=True, blank=True, editable=False)
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
