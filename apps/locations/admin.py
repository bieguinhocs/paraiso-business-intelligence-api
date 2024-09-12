from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AddressDepartment, AddressCity, AddressZonalGroup, AddressDistrict, Address
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display
from unfold.admin import TabularInline

class CityInline(TabularInline):
    model = AddressCity
    fields = ['name',]
    show_change_link = True
    can_delete = True
    tab = True
    extra = 0

@admin.register(AddressDepartment)
class AddressDepartmentAdmin(ModelAdmin):
    inlines = [CityInline]
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
        'display_department_header',
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

    @display(description=_('Department'), header=True)
    def display_department_header(self, instance: AddressDepartment):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

    @display(description=_('Created'))
    def display_created(self, instance: AddressDepartment):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

class DistrictInline(TabularInline):
    model = AddressDistrict
    fields = ['name', 'zonal_group', 'city', 'display_department']
    readonly_fields = ['display_department']
    autocomplete_fields = ['zonal_group', 'city',]
    show_change_link = True
    can_delete = True
    tab = True
    extra = 0

    @display(description=_('Department'))
    def display_department(self, instance: AddressDistrict):
        return instance.city.department

@admin.register(AddressCity)
class AddressCityAdmin(ModelAdmin):
    inlines = [DistrictInline]
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'name',
                    'department',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_city_header',
        'department',
        'display_created',
    )
    search_fields = (
        'name',
        'department__name',
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
    autocomplete_fields = (
        'department',
    )
    readonly_fields = (
        'created_at',
    )

    @display(description=_('City'), header=True)
    def display_city_header(self, instance: AddressCity):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

    @display(description=_('Created'))
    def display_created(self, instance: AddressCity):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('department__name', 'name',)
        for city in queryset:
            city.name = f"{city.department.name} - {city.name}"
        return queryset, use_distinct

@admin.register(AddressZonalGroup)
class AddressZonalGroupAdmin(ModelAdmin):
    inlines = [DistrictInline]
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
        'display_zonal_group_header',
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

    @display(description=_('Zonal group'), header=True)
    def display_zonal_group_header(self, instance: AddressZonalGroup):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

    @display(description=_('Created'))
    def display_created(self, instance: AddressZonalGroup):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('name')
        return queryset, use_distinct

@admin.register(AddressDistrict)
class AddressDistrictAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'), 
            {
                'fields': (
                    'name',
                    (
                        'city',
                        'display_department',
                    ),
                    'zonal_group',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_district_header',
        'city',
        'display_department',
        'zonal_group',
        'display_created',
    )
    search_fields = (
        'name',
        'city__name',
        'city__department__name',
        'zonal_group__name',
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
                    (
                        'city',
                        'display_department',
                    ),
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
    autocomplete_fields = (
        'city',
        'zonal_group',
    )
    readonly_fields = (
        'created_at',
        'display_department',
    )

    @display(description=_('District'), header=True)
    def display_district_header(self, instance: AddressDistrict):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

    @display(description=_('Department'))
    def display_department(self, instance: AddressDistrict):
        return instance.city.department

    @display(description=_('Created'))
    def display_created(self, instance: AddressDistrict):
        return instance.created_at
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.order_by('city__name', 'name',)
        for district in queryset:
            district.name = f"{district.city.department.name} - {district.city.name} - {district.name}"
        return queryset, use_distinct

@admin.register(Address)
class AddressAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    'name',
                    (
                        'district',
                        'display_zonal_group'
                    ),
                    (
                        'display_city',
                        'display_department',
                    ),
                ),
                'classes': ('wide',),
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
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_address_header',
        'district',
        'display_city',
        'display_department',
        'display_zonal_group',
        'display_created',
    )
    search_fields = (
        'name',
        'district__name',
        'district__city__name',
        'district__city__department__name',
        'district__zonal_group__name',
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
                    (
                        'district',
                        'display_zonal_group'
                    ),
                    (
                        'display_city',
                        'display_department',
                    ),
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
    autocomplete_fields = (
        'district',
    )
    readonly_fields = (
        'created_at',
        'display_city',
        'display_department',
        'display_zonal_group',
    )

    @display(description=_('Address'), header=True)
    def display_address_header(self, instance: Address):
        """
        Muestra el nombre en la primera línea.
        """
        return [
            instance.name,
            None,
            None,
        ]

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
