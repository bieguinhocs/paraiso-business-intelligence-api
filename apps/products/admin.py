from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    ProductGroup,
    ProductFamily,
    ProductBrand,
    ProductLine,
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
        'code',
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

@admin.register(ProductBrand)
class ProductBrandAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'code',
                    'name',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'code',
        'name',
        'display_created',
    )
    search_fields = (
        'code',
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
    def display_created(self, instance: ProductBrand):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(ProductLine)
class ProductLineAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'name',
                    'brand',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'name',
        'brand',
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
                    'brand',
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
        'brand',
    )
    readonly_fields = (
        'created_at',
    )

    @display(description=_('Created'))
    def display_created(self, instance: ProductLine):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'sku',
                    'name',
                    'size',
                    'color',
                    'line',
                    'family',
                    'retail',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'sku',
        'name',
        'size',
        'line',
        'family',
        'display_brand',
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
                    'sku',
                    'name',
                    'size',
                    'color',
                    'line',
                    'family',
                    'retail',
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
        'line',
        'family',
        'retail',
    )
    readonly_fields = (
        'created_at',
        'display_brand',
    )

    @display(description=_('Brand'))
    def display_brand(self, instance: Product):
        return instance.line.brand

    @display(description=_('Created'))
    def display_created(self, instance: Product):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct
   