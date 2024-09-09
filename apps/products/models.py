from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductGroup(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.name

class ProductFamily(models.Model):
    code = models.CharField(_('code'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=255, unique=True)
    group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, verbose_name=_('group'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('family')
        verbose_name_plural = _('families')

    def __str__(self):
        return self.name

class ProductBrand(models.Model):
    code = models.CharField(_('code'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __str__(self):
        return self.name

class ProductLine(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name=_('brand'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('line')
        verbose_name_plural = _('lines')

    def __str__(self):
        return self.name
    
class ProductSize(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')

    def __str__(self):
        return self.name
    
class ProductColor(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(_('SKU'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=255, unique=True)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, verbose_name=_('size'))
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, verbose_name=_('color'))
    line = models.ForeignKey(ProductLine, on_delete=models.CASCADE, verbose_name=_('line'))
    family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE, verbose_name=_('family'))
    retail = models.ForeignKey('stores.StoreRetail', on_delete=models.CASCADE, verbose_name=_('retail'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name
    
    @property
    def full_name(self):
        return f"{self.name} {self.size.name} {self.color}"
