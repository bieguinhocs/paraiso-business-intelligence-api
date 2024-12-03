from django.contrib import admin
from unfold.admin import ModelAdmin
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
from unfold.decorators import display
from django.templatetags.static import static
from unfold.admin import TabularInline

class FamilyInline(TabularInline):
    model = ProductFamily
    fields = ['code', 'name',]
    show_change_link = True
    can_delete = True
    tab = True
    extra = 0

@admin.register(ProductGroup)
class ProductGroupAdmin(ModelAdmin):
    inlines = [FamilyInline,]
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
        'display_group_header',
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

    @display(description=_('Group'), header=True)
    def display_group_header(self, instance: ProductGroup):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

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
        'display_family_header',
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

    @display(description=_('Family'), header=True)
    def display_family_header(self, instance: ProductFamily):
        """
        Muestra la familia en la primera línea, el codigo en la segunda.
        """
        return [
            instance.name,
            instance.code,
            None,
        ]

    @display(description=_('Created'))
    def display_created(self, instance: ProductFamily):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('group__name', 'name',)
        for family in queryset:
            family.name = f"{family.group.name} - {family.name}"
        return queryset, use_distinct

class LineInline(TabularInline):
    model = ProductLine
    fields = ['name',]
    show_change_link = True
    can_delete = True
    tab = True
    extra = 0

@admin.register(ProductBrand)
class ProductBrandAdmin(ModelAdmin):
    inlines = [LineInline,]
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
        'display_brand_header',
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

    @display(description=_('Brand'), header=True)
    def display_brand_header(self, instance: ProductBrand):
        """
        Muestra la marca en la primera línea, el codigo en la segunda,
        y un avatar en un círculo.
        """
        image_path = f"images/brands/{instance.name.lower()}.jpg"
        return [
            instance.name,
            instance.code,
            None,
            {
                "path": static(image_path),
                "squared": False,
                "borderless": True,
            }
        ]

    @display(description=_('Created'))
    def display_created(self, instance: ProductBrand):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

class ProductInline(TabularInline):
    model = Product
    fields = ['sku', 'display_product', 'retail', 'is_active']
    autocomplete_fields = ['retail',]
    readonly_fields = ['display_product',]
    show_change_link = True
    can_delete = True
    tab = True
    extra = 0
    max_num = 0

    @display(description=_('Name'))
    def display_product(self, instance: Product):
        return instance.full_name

@admin.register(ProductLine)
class ProductLineAdmin(ModelAdmin):
    inlines = [ProductInline,]
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
        'display_line_header',
        'display_brand_header',
        'display_created',
    )
    search_fields = (
        'name',
        'brand__name',
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
    
    @display(description=_('Line'), header=True)
    def display_line_header(self, instance: ProductLine):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

    @display(description=_('Brand'), header=True)
    def display_brand_header(self, instance: ProductLine):
        """
        Muestra la marca en la primera línea, el codigo en la segunda,
        y un avatar en un círculo.
        """
        image_path = f"images/brands/{instance.brand.name.lower()}.jpg"
        return [
            instance.brand.name,
            instance.brand.code,
            None,
            {
                "path": static(image_path),
                "squared": False,
                "borderless": True,
            }
        ]

    @display(description=_('Created'))
    def display_created(self, instance: ProductLine):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name', 'brand__name',)
        for line in queryset:
            line.name = f"{line.brand.name} - {line.name}"
        return queryset, use_distinct

@admin.register(ProductSize)
class ProductSizeAdmin(ModelAdmin):
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
        'display_size_header',
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

    @display(description=_('Size'), header=True)
    def display_size_header(self, instance: ProductSize):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

    @display(description=_('Created'))
    def display_created(self, instance: ProductSize):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(ProductColor)
class ProductColorAdmin(ModelAdmin):
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
        'display_color_header',
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

    @display(description=_('Color'), header=True)
    def display_color_header(self, instance: ProductColor):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

    @display(description=_('Created'))
    def display_created(self, instance: ProductColor):
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
                    (
                        'sku',
                        'name',
                    ),
                    (
                        'size',
                        'color',
                    ),
                    (
                        'line',
                        'display_brand',
                    ),
                    (
                        'family',
                        'display_group',
                    ),
                    'retail',
                    'description',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_product_header',
        'display_brand_header',
        'display_retail_header',
        'display_coverage_header',
        'display_created',
    )
    search_fields = (
        'sku',
        'name',
        'size__name',
        'color__name',
        'family__name',
        'line__name',   
        'line__brand__name',
    )
    list_filter = (
        'created_at',
    )
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    (
                        'sku',
                        'name',
                    ),
                    (
                        'size',
                        'color',
                    ),
                    (
                        'line',
                        'display_brand',
                    ),
                    (
                        'family',
                        'display_group',
                    ),
                    'retail',
                    'is_active',
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
    autocomplete_fields = (
        'size',
        'color',
        'line',
        'family',
        'retail',
    )
    readonly_fields = (
        'created_at',
        'display_brand',
        'display_group',
    )

    @display(description=_('Product'), header=True)
    def display_product_header(self, instance: Product):
        """
        Muestra el nombre completo en la primera línea, el sku en la segunda,
        y un avatar en un círculo.
        """
        return [
            instance.full_name,
            instance.sku,
            None,
            {
                "path": static("images/products/dormitorio.jpg"),
                "squared": False,
                "borderless": True,
            }
        ]
    
    @display(description=_('Brand'), header=True)
    def display_brand_header(self, instance: Product):
        """
        Muestra la marca en la primera línea, el codigo en la segunda,
        y un avatar en un círculo.
        """
        image_path = f"images/brands/{instance.line.brand.name.lower()}.jpg"
        return [
            instance.line.brand.name,
            instance.line.brand.code,
            None,
            {
                "path": static(image_path),
                "squared": False,
                "borderless": True,
            }
        ]

    @display(description=_('Retail'), header=True)
    def display_retail_header(self, instance: Product):
        """
        Muestra el retail en la primera línea, el canal en la segunda,
        y un avatar en un círculo.
        """
        if instance.retail:
            image_path = f"images/retails/{instance.retail.name.lower()}.jpg"
            return [
                instance.retail.name,
                instance.retail.channel.name,     
                None,
                {
                    "path": static(image_path),
                    "squared": False,
                    "borderless": True,
                }
            ]
        return []

    @display(
        description=_('Status'),
        label={
            _('inactive'): 'danger',
            _('active'): 'success',
        },
    )
    def display_coverage_header(self, instance: Product):
        return _('active') if instance.is_active else _('inactive')

    @display(description=_('Brand'))
    def display_brand(self, instance: Product):
        return instance.line.brand
    
    @display(description=_('Group'))
    def display_group(self, instance: Product):
        return instance.family.group

    @display(description=_('Created'))
    def display_created(self, instance: Product):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct
        