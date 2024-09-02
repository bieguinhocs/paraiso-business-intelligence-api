from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AddressDepartment, AddressCity, AddressZonalGroup, AddressDistrict, Address
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display

@admin.register(AddressDepartment)
class AddressDepartmentAdmin(ModelAdmin):
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
    def display_created(self, instance: AddressDepartment):
        return instance.created_at

@admin.register(AddressCity)
class AddressCityAdmin(ModelAdmin):
    list_display = (
        'name',
        'department',
        'display_created',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'department',
        'created_at',
    )
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    'name',
                    'department',
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
    def display_created(self, instance: AddressCity):
        return instance.created_at

@admin.register(AddressZonalGroup)
class AddressZonalGroupAdmin(ModelAdmin):
    list_display = (
        'name',
        'display_created',
    )
    search_fields = (
        'name',
        'created_at',
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
    def display_created(self, instance: AddressZonalGroup):
        return instance.created_at

@admin.register(AddressDistrict)
class AddressDistrictAdmin(ModelAdmin):
    list_display = (
        'name',
        'city',
        'display_department',
        'zonal_group',
        'display_created',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'city',
        'city__department',
        'zonal_group',
        'created_at',
    )
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    'name',
                    'city',
                    'zonal_group',
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

    @display(description=_('Department'))
    def display_department(self, instance: AddressDistrict):
        return instance.city.department

    @display(description=_('Created'))
    def display_created(self, instance: AddressDistrict):
        return instance.created_at

@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = (
        'name',
        'district',
        'display_city',
        'display_department',
        'display_zonal_group',
        'display_created',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'district',
        'district__city',
        'district__city__department',
        'created_at',
    )
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    'name',
                    'district',
                    #'district__city',
                ),
                'classes': ['tab',],
            },
        ),
        (
            _('Location'),
            {
                'fields': (
                    (
                        'latitude',
                        'longitude',
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
    readonly_fields = (
        'created_at',
    )

    @display(description=_('Created'))
    def display_created(self, instance: Address):
        return instance.created_at

    @display(description=_('City'))
    def display_city(self, instance: Address):
        return instance.district.city
    
    @display(description=_('Department'))
    def display_department(self, instance: Address):
        return instance.district.city.department
    
    @display(description=_('Zonal group'))
    def display_zonal_group(self, instance: Address):
        return instance.district.zonal_group
