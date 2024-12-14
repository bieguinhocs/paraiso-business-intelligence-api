from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from utils.text_format import format_to_title_case
from django.core.validators import MaxValueValidator, MinValueValidator

class SaleType(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('sale type')
        verbose_name_plural = _('sale types')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class SaleSource(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('sale source')
        verbose_name_plural = _('sale sources')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class SaleStatus(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('sale status')
        verbose_name_plural = _('sale statuses')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class SalePriceType(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('sale price type')
        verbose_name_plural = _('sale price types')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Sale(models.Model):
    sale_date = models.DateTimeField(_('sale date'), blank=True, null=True)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, verbose_name=_('store'))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('promoter'), null=True)
    sale_type = models.ForeignKey(SaleType, on_delete=models.CASCADE, verbose_name=_('type'), null=True)
    source = models.ForeignKey(SaleSource, on_delete=models.CASCADE, verbose_name=_('source'), null=True)
    sale_status = models.ForeignKey(SaleStatus, on_delete=models.CASCADE, verbose_name=_('status'), null=True)
    comment = models.TextField(_('comment'), blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('sale')
        verbose_name_plural = _('sales')

    def __str__(self):
        return f"Venta {self.id} por {self.user} en {self.sale_date}"

class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='details', verbose_name=_('sale'))
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name=_('product'))
    unit_price = models.DecimalField(_('unit price'), max_digits=6, decimal_places=2)
    quantity = models.IntegerField(_('quantity'), validators=[MinValueValidator(1), MaxValueValidator(100)])
    price_type = models.ForeignKey(SalePriceType, on_delete=models.CASCADE, verbose_name=_('price type'))

    class Meta:
        verbose_name = _('sale detail')
        verbose_name_plural = _('sale details')

    def __str__(self):
        return f"{self.quantity} x {self.product} en {self.sale}"
