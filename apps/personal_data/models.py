from django.db import models
from django.utils.translation import gettext_lazy as _
from sales.models import Sale

class PersonalData(models.Model):
    sale = models.OneToOneField(
        Sale,
        on_delete=models.CASCADE,
        verbose_name=_('sale'),
        related_name='personal_data'
    )
    client_first_name = models.CharField(_('first name'), max_length=255)
    client_last_name = models.CharField(_('last name'), max_length=255)
    client_document_type = models.CharField(_('document type'), max_length=50)
    client_document = models.CharField(_('document number'), max_length=50, unique=True)
    client_phone = models.CharField(_('phone number'), max_length=20, blank=True, null=True)
    client_email = models.EmailField(_('email'), blank=True, null=True)
    answer_1 = models.TextField(_('answer 1'), blank=True, null=True)
    answer_2 = models.TextField(_('answer 2'), blank=True, null=True)
    photo = models.ImageField(
        _('photo'),
        upload_to='client_photos/',
        blank=True,
        null=True,
        help_text=_('Photo of the client (optional)')
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('personal data')
        verbose_name_plural = _('personal data')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_first_name} {self.client_last_name} - {self.client_document}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)