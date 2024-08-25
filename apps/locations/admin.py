from django.contrib import admin
from .models import AddressDepartment, AddressCity, AddressZoneGroup, AddressDistrict, Address

# Filtro por Distrito en AddressAdmin
class DistrictFilter(admin.SimpleListFilter):
    title = 'Distrito'
    parameter_name = 'district'

    def lookups(self, request, model_admin):
        districts = AddressDistrict.objects.all()
        return [(d.id, d.name) for d in districts]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(district__id=self.value())
        return queryset

# Filtro por Ciudad en AddressAdmin (a través de District)
class CityFilterForAddress(admin.SimpleListFilter):
    title = 'Ciudad'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = AddressCity.objects.all()
        return [(c.id, c.name) for c in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(district__city__id=self.value())
        return queryset

# Filtro por Departamento en AddressAdmin (a través de City y District)
class DepartmentFilterForAddress(admin.SimpleListFilter):
    title = 'Departamento'
    parameter_name = 'department'

    def lookups(self, request, model_admin):
        departments = AddressDepartment.objects.all()
        return [(d.id, d.name) for d in departments]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(district__city__department__id=self.value())
        return queryset

# Filtro por Ciudad en AddressDistrictAdmin
class CityFilterForDistrict(admin.SimpleListFilter):
    title = 'Ciudad'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = AddressCity.objects.all()
        return [(c.id, c.name) for c in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(city__id=self.value())
        return queryset

# Filtro por Departamento en AddressCityAdmin
class DepartmentFilterForCity(admin.SimpleListFilter):
    title = 'Departamento'
    parameter_name = 'department'

    def lookups(self, request, model_admin):
        departments = AddressDepartment.objects.all()
        return [(d.id, d.name) for d in departments]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(department__id=self.value())
        return queryset

@admin.register(AddressDepartment)
class AddressDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(AddressCity)
class AddressCityAdmin(admin.ModelAdmin):
    list_display = ('name', 'department',)
    search_fields = ('name',)
    list_filter = (DepartmentFilterForCity, 'created_at',)

@admin.register(AddressZoneGroup)
class AddressZoneGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'created_at',)
    list_filter = ('created_at',)

@admin.register(AddressDistrict)
class AddressDistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'get_department', 'zone_group',)
    search_fields = ('name',)
    list_filter = (CityFilterForDistrict, 'zone_group', 'created_at',)

    def get_department(self, obj):
        return obj.city.department.name
    get_department.short_description = 'Departamento'

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'get_city', 'get_department', 'get_zone_group',)
    search_fields = ('name',)
    list_filter = (DistrictFilter, CityFilterForAddress, DepartmentFilterForAddress, 'created_at',)

    def get_city(self, obj):
        return obj.district.city.name
    get_city.short_description = 'Ciudad'

    def get_department(self, obj):
        return obj.district.city.department.name
    get_department.short_description = 'Departamento'

    def get_zone_group(self, obj):
        return obj.district.zone_group.name
    get_zone_group.short_description = 'Grupo Zonal'
