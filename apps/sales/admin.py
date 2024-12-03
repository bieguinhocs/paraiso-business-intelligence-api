from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    SaleType,
    SaleSource,
    SaleStatus,
    SalePriceType,
    Sale,
    SaleDetail,
)
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display
from unfold.admin import TabularInline

@admin.register(SaleType)
class SaleTypeAdmin(ModelAdmin):
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
    def display_created(self, instance: SaleType):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(SaleSource)
class SaleSourceAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'name',
                    'description',
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
                    'description',
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
    def display_created(self, instance: SaleSource):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(SaleStatus)
class SaleStatusAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'name',
                    'description',
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
                    'description',
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
    def display_created(self, instance: SaleStatus):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(SalePriceType)
class SalePriceTypeAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'name',
                    'description',
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
                    'description',
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
    def display_created(self, instance: SalePriceType):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

class SaleDetailInline(TabularInline):
    model = SaleDetail
    fields = ('product', 'unit_price', 'quantity', 'price_type')
    autocomplete_fields = ['product', 'price_type',]
    tab = True
    extra = 1
    min_num = 1
    validate_min = True

@admin.register(Sale)
class SaleAdmin(ModelAdmin):
    inlines = [SaleDetailInline]
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'store',
                    'sale_date',
                    'comment',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_store_header',
        'sale_date',
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
                    'store',
                    'sale_date',
                    'comment',
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
        'store',
    )
    readonly_fields = (
        'created_at',
    )

    @display(description=_('Store'))
    def display_store_header(self, instance: Sale):
        return instance.store.full_name

    @display(description=_('Created'))
    def display_created(self, instance: Sale):
        return instance.created_at
    
    #def get_search_results(self, request, queryset, search_term):
    #    queryset, use_distinct = super().get_search_results(request, queryset, search_term)
    #    queryset = queryset.order_by('name')
    #    return queryset, use_distinct
         