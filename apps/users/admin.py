from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

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

admin.site.register(CustomUser, CustomUserAdmin)