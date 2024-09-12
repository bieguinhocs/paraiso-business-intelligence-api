from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from utils.text_format import format_to_title_case

class AddressDepartment(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class AddressCity(models.Model):
    name = models.CharField(_('name'), max_length=255)
    department = models.ForeignKey(AddressDepartment, on_delete=models.CASCADE, verbose_name=_('department'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class AddressZonalGroup(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('zonal group')
        verbose_name_plural = _('zonal groups')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class AddressDistrict(models.Model):
    name = models.CharField(_('name'), max_length=255)
    city = models.ForeignKey(AddressCity, on_delete=models.CASCADE, verbose_name=_('city'))
    zonal_group = models.ForeignKey(AddressZonalGroup, on_delete=models.CASCADE, verbose_name=_('zonal group'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('district')
        verbose_name_plural = _('districts')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Address(models.Model):
    name = models.CharField(_('name'), max_length=255)
    latitude = models.DecimalField(_('latitude'), max_digits=8, decimal_places=6, default=0.0)
    longitude = models.DecimalField(_('longitude'), max_digits=9, decimal_places=6, default=0.0)
    district = models.ForeignKey(AddressDistrict, on_delete=models.CASCADE, verbose_name=_('district'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return self.name or self.location
    
    def validate_latitude_longitude(self):
        if not (-90 <= self.latitude <= 90):
            raise ValidationError('Latitude must be between -90 and 90 degrees.')
        if not (-180 <= self.longitude <= 180):
            raise ValidationError('Longitude must be between -180 and 180 degrees.')

    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)
        self.validate_latitude_longitude()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)