from django.contrib import admin
from api.admin import custom_admin_site
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import CustomUser

# Registrar el modelo User con su correspondiente UserAdmin
custom_admin_site.register(User, UserAdmin)

# Registrar el modelo Group con su correspondiente GroupAdmin
custom_admin_site.register(Group, GroupAdmin)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Acceso y Seguridad', {'fields': ('username', 'password', 'last_login')}),
        ('Datos Personales', {'fields': ('dni', 'first_name', 'last_name', 'email', 'corporate_phone', 'corporate_device_imei', 'supervisor')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('employment_start_date', 'employment_end_date', 'created_at')}),
    )
    readonly_fields = ('created_at',)

    # Campos visibles en la lista de usuarios
    list_display = UserAdmin.list_display + ('is_active',)

custom_admin_site.register(CustomUser, CustomUserAdmin)