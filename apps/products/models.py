from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductGroup(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.name

class ProductFamily(models.Model):
    code = models.CharField(_('code'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=255, unique=True)
    group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, verbose_name=_('group'))

    class Meta:
        verbose_name = _('family')
        verbose_name_plural = _('families')

    def __str__(self):
        return self.name

class ProductLine(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('line')
        verbose_name_plural = _('lines')

    def __str__(self):
        return self.name

class ProductBrand(models.Model):
    code = models.CharField(_('code'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(_('SKU'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=255, unique=True)
    size = models.CharField(_('size'), max_length=50, blank=True, null=True)
    color = models.CharField(_('color'), max_length=50, blank=True, null=True)
    line = models.ForeignKey(ProductLine, on_delete=models.CASCADE, verbose_name=_('line'))
    family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE, verbose_name=_('family'))
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name=_('brand'))
    retail = models.ForeignKey('stores.StoreRetail', on_delete=models.CASCADE, verbose_name=_('retail'))
    
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name
