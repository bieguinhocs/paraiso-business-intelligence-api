from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    StoreChannel,
    StoreRetail,
    Store
)
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display
from django.templatetags.static import static
from unfold.admin import TabularInline

class RetailInline(TabularInline):
    model = StoreRetail
    fields = ['code', 'name', 'business_name']
    show_change_link = True
    can_delete = True
    tab = True
    extra = 0

@admin.register(StoreChannel)
class StoreChannelAdmin(ModelAdmin):
    inlines = [RetailInline]
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
    def display_created(self, instance: StoreChannel):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

class StoreInline(TabularInline):
    model = Store
    fields = ['name', 'coordinator', 'is_covered']
    autocomplete_fields = ['coordinator']
    show_change_link = True
    can_delete = True
    tab = True
    extra = 0

@admin.register(StoreRetail)
class StoreRetailAdmin(ModelAdmin):
    inlines = [StoreInline]
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    (
                        'name',
                        'business_name',
                    ),
                    (
                        'ruc',
                        'channel',
                    ),
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_retail_header',
        'business_name',
        'ruc',
        'display_created',
    )
    search_fields = (
        'name',
        'business_name',
        'ruc',
        'channel__name',
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
                        'name',
                        'business_name',
                    ),
                    (
                        'ruc',
                        'channel',
                    ),      
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
        'channel',
    )
    readonly_fields = (
        'created_at',
    )

    @display(description=_('Name'), header=True)
    def display_retail_header(self, instance: StoreRetail):
        """
        Muestra el nombre en la primera línea, el canal en la segunda,
        y un avatar en un círculo.
        """
        image_path = f"images/retails/{instance.name.lower()}.jpg"
        return [
            instance.name,
            instance.channel,
            None,
            {
                "path": static(image_path),
                "squared": False,
                "borderless": True,
            }
        ]

    @display(description=_('Created'))
    def display_created(self, instance: StoreRetail):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(Store)
class StoreAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    (
                        'name',
                        'sellout_name',
                    ),
                    (
                        'retail',
                        'display_channel',
                    ),
                    'address',
                ),
                'classes': ('wide',),
            },
        ),
        (
            _('Operational Team'),
            {
                'fields': (
                    (
                        'coordinator',
                        'promoters',
                    )
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_store_header',
        'display_coordinator_header',
        'display_coverage_header',
        'display_created',
    )
    search_fields = (
        'name',
        'retail__name',
        'coordinator__first_name',
        'coordinator__last_name',
    )
    list_filter = (
        'retail',
        'created_at',
    )
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (      
                    (
                        'name',
                        'sellout_name',
                    ),
                    (
                        'retail',
                        'display_channel',
                    ),
                        'address',
                        'is_covered',
                ),
                'classes': ['tab',],
            },
        ),
        (
            _('Operational Team'),
            {
                'fields': (
                    (
                        'coordinator',
                        'promoters',
                    )
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
        'retail',
        'coordinator',  
        'address',
        'promoters',
    )
    readonly_fields = (
        'created_at',
        'display_channel'
    )

    @display(description=_('Name'), header=True)
    def display_store_header(self, instance: Store):
        """
        Muestra cadena+nombre en la primera línea, el canal en la segunda,
        y un avatar en un círculo.
        """
        image_path = f"images/retails/{instance.retail.name.lower()}.jpg"
        return [
            instance.full_name,
            instance.retail.channel,
            None,
            {
                "path": static(image_path),
                "squared": False,
                "borderless": True,
            }
        ]
    
    @display(description=_('Coordinator'), header=True)
    def display_coordinator_header(self, instance: Store):
        """
        Muestra el nombre completo en la primera línea, el usuario en la segunda,
        y un avatar en un círculo.
        """
        return [
            instance.coordinator.full_name,
            instance.coordinator.get_username,
            None,
            {
                "path": static("images/avatar.jpg"),
                "squared": False,
                "borderless": True,
            }
        ]

    @display(
        description=_('Coverage'),
        label={
            _('inactive'): 'danger',
            _('active'): 'success',
        },
    )
    def display_coverage_header(self, instance: Store):
        return _('active') if instance.is_covered else _('inactive')

    @display(description=_('Channel'))
    def display_channel(self, instance: Store):
        return instance.retail.channel

    @display(description=_('Created'))
    def display_created(self, instance: Store):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('retail__name', 'name')
        return queryset, use_distinct
