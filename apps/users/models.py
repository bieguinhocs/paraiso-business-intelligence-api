from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

def validate_document_number(value, document_type):
    if document_type == 'DNI' and len(value) != 8:
        raise ValidationError(_('Document number must be exactly 8 digits for DNI.'))
    elif document_type == 'CE' and len(value) != 9:
        raise ValidationError(_('Document number must be exactly 9 digits for foreigner card.'))

class CustomUser(AbstractUser):
    DOCUMENT_TYPE_CHOICES = [
        ('DNI', 'DNI'),
        ('CE', _('foreigner card')),
    ]
    document_type = models.CharField(_('document type'), max_length=3, choices=DOCUMENT_TYPE_CHOICES)
    document_number = models.CharField(_('document number'), max_length=9, unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    corporate_phone = models.CharField(_('corporate phone number'), max_length=9, validators=[MinLengthValidator(9)], blank=True, null=True)
    corporate_device_imei = models.CharField(_('corporate device imei'), max_length=15, validators=[MinLengthValidator(15)], blank=True, null=True)
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

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.last_name}, {self.first_name}"
        return None
    
    def clean(self):
        super().clean()
        validate_document_number(self.document_number, self.document_type)