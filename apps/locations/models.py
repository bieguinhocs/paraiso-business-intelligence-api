from django.db import models
from django.utils.translation import gettext_lazy as _

class AddressDepartment(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')

    def __str__(self):
        return self.name

class AddressCity(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    department = models.ForeignKey(AddressDepartment, on_delete=models.CASCADE, verbose_name=_('department'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __str__(self):
        return self.name

class AddressZoneGroup(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('zonal group')
        verbose_name_plural = _('zonal groups')

    def __str__(self):
        return self.name

class AddressDistrict(models.Model):
    name = models.CharField(_('name'), max_length=255)
    city = models.ForeignKey(AddressCity, on_delete=models.CASCADE, verbose_name=_('city'))
    zone_group = models.ForeignKey(AddressZoneGroup, on_delete=models.CASCADE, verbose_name='zonal group')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('district')
        verbose_name_plural = _('districts')

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(_('name'), max_length=255, blank=True, null=True)
    location = models.CharField(_('location'), max_length=255, blank=True, null=True)
    district = models.ForeignKey(AddressDistrict, on_delete=models.CASCADE, verbose_name='district')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return self.name or self.location
    