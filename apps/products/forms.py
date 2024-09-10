from django import forms
from unfold.widgets import UnfoldAdminSelectWidget
from .models import (
    ProductGroup,
    ProductFamily,
    ProductBrand,
    ProductLine,
    ProductSize,
    ProductColor,
    Product
)
from django.utils.translation import gettext_lazy as _

class ProductAdminForm(forms.ModelForm):
    # Campo de brand solo para el formulario, no está en el modelo Product
    brand = forms.ModelChoiceField(
        queryset=ProductBrand.objects.all(),
        required=True,
        label=_('Brand'),
        widget=UnfoldAdminSelectWidget(attrs={'id': 'id_brand'})
    )

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'line': UnfoldAdminSelectWidget(),
        }

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',  # Añadir jQuery si no está disponible
            'admin/js/dynamic_brand_line.js',
        )
