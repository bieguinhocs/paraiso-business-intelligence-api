from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from utils.text_format import format_to_title_case
from .validators import validate_ruc

class StoreChannel(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('channel')
        verbose_name_plural = _('channels')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class StoreRetail(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    business_name = models.CharField(_('business name'), max_length=255, blank=True, null=True)
    ruc = models.CharField(_('RUC'), max_length=11, unique=False, validators=[validate_ruc])
    channel = models.ForeignKey(StoreChannel, on_delete=models.CASCADE, verbose_name=_('channel'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('retail')
        verbose_name_plural = _('retails')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Store(models.Model):
    name = models.CharField(_('name'), max_length=255)
    sellout_name = models.CharField(_('sellout name'), max_length=255, blank=True, null=True)
    address = models.ForeignKey('locations.Address', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('address'))
    coordinator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='coordinator_stores', verbose_name=_('coordinator'))
    retail = models.ForeignKey(StoreRetail, on_delete=models.CASCADE, verbose_name=_('retail'))
    is_covered = models.BooleanField(_('coverage'), default=True, help_text=_('Indicates whether this store is covered. Uncheck this option if it is not covered.'))
    promoters = models.ManyToManyField(get_user_model(), blank=True, null=True, related_name='promoter_stores', verbose_name=_('promoters'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('store')
        verbose_name_plural = _('stores')

    def __str__(self):
        return self.name
    
    @property
    def full_name(self):
        return f"{self.retail.name} {self.name}"
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
