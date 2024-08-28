from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import CustomUser

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class UserAdmin(UserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(GroupAdmin, ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    fieldsets = (
        ('Acceso y Seguridad', {'fields': ('username', 'password', 'last_login')}),
        ('Datos Personales', {'fields': ('dni', 'first_name', 'last_name', 'email', 'corporate_phone', 'corporate_device_imei', 'supervisor')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('employment_start_date', 'employment_end_date', 'created_at')}),
    )
    readonly_fields = ('created_at',)

    # Campos visibles en la lista de usuarios
    list_display = UserAdmin.list_display + ('is_active',)
