from django.db import models
from sales.models import Sale
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from utils.text_format import format_to_title_case
from utils.validators import validate_only_digits, validate_document_number
from utils.constants import DOCUMENT_TYPE_CHOICES

class PersonalData(models.Model):
    client_first_name = models.CharField(_('client first name'), max_length=255)
    client_last_name = models.CharField(_('client last name'), max_length=255)
    client_document_type = models.CharField(_('client document type'), max_length=3, choices=DOCUMENT_TYPE_CHOICES)
    client_document_number = models.CharField(_('client document number'), max_length=9, unique=True)
    client_phone = models.CharField(_('client phone number'), max_length=9, validators=[validate_only_digits, MinLengthValidator(9)], blank=True, null=True)
    client_email = models.EmailField(_('client email'), blank=True, null=True)
    answer_1 = models.TextField(_('answer 1'), blank=True, null=True)
    answer_2 = models.TextField(_('answer 2'), blank=True, null=True)
    photo = models.ImageField(
        _('survey photo'),
        upload_to='personal_data_survey_photos/',
        blank=False,
        null=False,
        help_text=_('Photo of the personal data survey')
    )
    sale = models.OneToOneField(
        Sale,
        on_delete=models.CASCADE,
        verbose_name=_('sale'),
        related_name='personal_data'
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('personal data survey')
        verbose_name_plural = _('personal data surveys')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_first_name} {self.client_last_name} - {self.client_document_number}"

    def clean(self):
        super().clean()
        validate_document_number(self.client_document_number, self.client_document_type)

    def save(self, *args, **kwargs):
        self.client_first_name = format_to_title_case(self.client_first_name)
        self.client_last_name = format_to_title_case(self.client_last_name)
        super().save(*args, **kwargs)