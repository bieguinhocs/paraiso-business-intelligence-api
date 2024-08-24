from django.contrib import admin
from .models import AddressDepartment, AddressCity, AddressZoneGroup, AddressDistrict, Address

@admin.register(AddressDepartment)
class AddressDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(AddressCity)
class AddressCityAdmin(admin.ModelAdmin):
    list_display = ('name', 'department',)
    search_fields = ('name',)
    list_filter = ('department',)

@admin.register(AddressZoneGroup)
class AddressZoneGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(AddressDistrict)
class AddressDistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'zone_group',)
    search_fields = ('name',)
    list_filter = ('city', 'zone_group')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'district',)
    search_fields = ('name',)
    list_filter = ('district',)
