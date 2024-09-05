from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class StoreChannel(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        verbose_name = _('store channel')
        verbose_name_plural = _('store channels')

    def __str__(self):
        return self.name

class StoreRetail(models.Model):
    code = models.CharField(_('code'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=255, unique=True)
    business_name = models.CharField(_('business name'), max_length=255, blank=True, null=True)
    channel = models.ForeignKey(StoreChannel, on_delete=models.CASCADE, verbose_name=_('channel'))

    class Meta:
        verbose_name = _('store retail')
        verbose_name_plural = _('store retails')

    def __str__(self):
        return self.name

class StoreCoverage(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('store coverage')
        verbose_name_plural = _('store coverages')

    def __str__(self):
        return self.name

class Store(models.Model):
    code = models.CharField(_('code'), max_length=100, unique=True, blank=True, null=True)
    name = models.CharField(_('name'), max_length=255, unique=True)
    sellout_name = models.CharField(_('sellout name'), max_length=255, blank=True, null=True)
    address = models.ForeignKey('locations.Address', on_delete=models.CASCADE, verbose_name=_('address'))
    coordinator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='coordinator_stores', verbose_name=_('coordinator'))
    retail = models.ForeignKey(StoreRetail, on_delete=models.CASCADE, verbose_name=_('retail'))
    coverage = models.ForeignKey(StoreCoverage, on_delete=models.CASCADE, verbose_name=_('coverage'))
    promoters = models.ManyToManyField(get_user_model(), related_name='promoter_stores', verbose_name=_('promoters'))

    class Meta:
        verbose_name = _('store')
        verbose_name_plural = _('stores')

    def __str__(self):
        return self.name
