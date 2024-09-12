from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from utils.text_format import format_to_title_case
import re

def validate_numeric_digits(value):
    if not re.fullmatch(r'\d+', value):
        raise ValidationError(_('The code must contain only numeric digits.'))

def validate_three_digit_code(value):
    if not re.fullmatch(r'\d{3}', value):
        raise ValidationError(_('The code must be exactly 3 digits, and only numbers are allowed.'))

class ProductGroup(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class ProductFamily(models.Model):
    code = models.CharField(_('code'), max_length=3, unique=True, validators=[validate_three_digit_code])
    name = models.CharField(_('name'), max_length=255, unique=True)
    group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, verbose_name=_('group'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('family')
        verbose_name_plural = _('families')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class ProductBrand(models.Model):
    code = models.CharField(_('code'), max_length=3, unique=True, validators=[validate_three_digit_code])
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class ProductLine(models.Model):
    name = models.CharField(_('name'), max_length=255)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name=_('brand'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('line')
        verbose_name_plural = _('lines')
        constraints = [
            models.UniqueConstraint(fields=['name'], name='nombre único', condition=~models.Q(name='-'))
        ]

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
class ProductSize(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
class ProductColor(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Product(models.Model):
    sku = models.CharField(_('SKU'), max_length=100, blank=True, null=True, validators=[validate_numeric_digits])
    name = models.CharField(_('name'), max_length=255)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, verbose_name=_('size'))
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('color'))
    line = models.ForeignKey(ProductLine, on_delete=models.CASCADE, verbose_name=_('line'))
    family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE, verbose_name=_('family'))
    retail = models.ForeignKey('stores.StoreRetail', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('retail'))
    is_active = models.BooleanField(_('status'), default=True, help_text=_('Indicates whether this product is active. Uncheck this option if it is not active.'))
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        constraints = [
            models.UniqueConstraint(fields=['sku'], name='sku único', condition=models.Q(sku__isnull=False))
        ]

    def __str__(self):
        return self.name
    
    @property
    def full_name(self):
        line_val = f' {self.line.name}' if self.line.name != '-' else ''
        color_val = f' {self.color}' if self.color else ''
        return f"{self.family}{line_val} {self.name} {self.size}{color_val}"
    
    def clean(self):
        super().clean()
        self.name = format_to_title_case(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
