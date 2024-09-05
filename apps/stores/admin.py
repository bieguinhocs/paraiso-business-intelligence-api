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

@admin.register(StoreChannel)
class StoreChannelAdmin(ModelAdmin):
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

@admin.register(StoreRetail)
class StoreRetailAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    (
                        'code',
                        'channel',
                    ),
                    (
                        'name',
                        'business_name',
                    ),
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'code',
        'name',
        'business_name',
        'channel',
        'display_created',
    )
    search_fields = (
        'code',
        'name',
        'business_name',
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
                        'code',
                        'channel',
                    ),
                    (
                        'name',
                        'business_name',
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

    @display(description=_('Created'))
    def display_created(self, instance: StoreRetail):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('code', 'name')
        return queryset, use_distinct

@admin.register(Store)
class StoreAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                        'code',
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
        'code',
        'name',
        'retail',
        'display_coordinator',
        'display_coverage',
        'display_created',
    )
    search_fields = (
        'code',
        'name',
        'retail',
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

    @display(description=_('Channel'))
    def display_channel(self, instance: Store):
        return instance.retail.channel
    
    @display(description=_('Coordinator'), header=True)
    def display_coordinator(self, instance: Store):
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
    def display_coverage(self, instance: Store):
        return _('active') if instance.is_covered else _('inactive')

    @display(description=_('Created'))
    def display_created(self, instance: Store):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('code', 'name')
        return queryset, use_distinct
