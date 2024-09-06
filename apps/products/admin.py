from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    ProductGroup,
    ProductFamily,
    ProductLine,
    ProductBrand,
    Product
)
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display
from django.templatetags.static import static

@admin.register(ProductGroup)
class ProductGroupAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'name',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'name',
        'display_created',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'created_at',
    )
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    'name',
                ),
                'classes': ['tab',],
            },
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'created_at',
                ),
                'classes': ['tab',],
            },
        ),
    )
    readonly_fields = (
        'created_at',
    )

    @display(description=_('Created'))
    def display_created(self, instance: ProductGroup):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(ProductFamily)
class ProductFamilyAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'code',
                    'name',
                    'group',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'code',
        'name',
        'group',
        'display_created',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'created_at',
    )
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    'code',
                    'name',
                    'group',
                ),
                'classes': ['tab',],
            },
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'created_at',
                ),
                'classes': ['tab',],
            },
        ),
    )
    autocomplete_fields = (
        'group',
    )
    readonly_fields = (
        'created_at',
    )

    @display(description=_('Created'))
    def display_created(self, instance: ProductFamily):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct
    