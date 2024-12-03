from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.validators import MinLengthValidator
from utils.text_format import format_to_title_case
from utils.validators import validate_only_digits, validate_document_number
from utils.constants import DOCUMENT_TYPE_CHOICES

@receiver(pre_save, sender=Group)
def format_group_name(sender, instance, **kwargs):
    instance.name = format_to_title_case(instance.name)

class CustomUser(AbstractUser):
    document_type = models.CharField(_('document type'), max_length=3, choices=DOCUMENT_TYPE_CHOICES)
    document_number = models.CharField(_('document number'), max_length=9, unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    corporate_phone = models.CharField(_('corporate phone number'), max_length=9, validators=[validate_only_digits, MinLengthValidator(9)], blank=True, null=True)
    corporate_device_imei = models.CharField(_('corporate device imei'), max_length=15, validators=[MinLengthValidator(15)], blank=True, null=True)
    employment_start_date = models.DateTimeField(_('employment start'), blank=True, null=True)
    employment_end_date = models.DateTimeField(_('employment end'), blank=True, null=True)
    address = models.ForeignKey('locations.Address', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('address'))
    coordinator = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('coordinator'))
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
    
    @property
    def groups_list(self):
        # Devuelve una lista con los grupos a los que pertenece el usuario
        return ", ".join([group.name for group in self.groups.all()])
    
    def clean(self):
        super().clean()
        validate_document_number(self.document_number, self.document_type)
        
    def save(self, *args, **kwargs):
        self.first_name = format_to_title_case(self.first_name)
        self.last_name = format_to_title_case(self.last_name)
        super().save(*args, **kwargs)