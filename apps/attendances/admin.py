from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static
from unfold.admin import TabularInline
from .forms import AttendanceForm
from .models import (
    Attendance,
    AttendanceRecordType,
    AttendanceAccessType
)

@admin.register(AttendanceRecordType)
class AttendanceRecordTypeAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'),
            {
                'fields': ('name', 'description'),
                'classes': ('wide',),
            },
        ),
    )
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    @display(description=_('Created'))
    def display_created(self, instance: AttendanceRecordType):
        return instance.created_at


@admin.register(AttendanceAccessType)
class AttendanceAccessTypeAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'),
            {
                'fields': ('name', 'description'),
                'classes': ('wide',),
            },
        ),
    )
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    @display(description=_('Created'))
    def display_created(self, instance: AttendanceAccessType):
        return instance.created_at


@admin.register(Attendance)
class AttendanceAdmin(ModelAdmin):
    form = AttendanceForm
    class Media:
        js = ('js/photo_preview.js',)
    add_fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    ('user', 'store'),
                    ('record_type', 'access_type'),
                    'photo',
                    'automatic',
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_user_header',
        'display_store_header',
        'display_autimatic_header',
        'created_at',
    )
    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'store__name',
    )
    list_filter = (
        'record_type',
        'access_type',
        'automatic',
        'created_at',
    )
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    ('user', 'store'),
                    ('record_type', 'access_type'),
                    'photo',
                    'automatic',
                ),
                'classes': ['tab'],
            },
        ),
        (
            _('Important dates'),
            {
                'fields': ('created_at',),
                'classes': ['tab'],
            },
        ),
    )
    autocomplete_fields = ('user', 'store', 'record_type', 'access_type')
    readonly_fields = ('created_at',)

    @display(description=_('Attendance'), header=True)
    def display_user_header(self, instance: Attendance):
        """
        Muestra el nombre completo del usuario y una concatenación
        de attendance_record_type y attendance_access_type.
        """
        return [
            f"{instance.user.first_name} {instance.user.last_name}",
            f"{instance.access_type.name} {instance.record_type.name}",
            None,
            {
                "path": static("images/avatar.jpg"),
                "squared": False,
                "borderless": True,
            },
        ]

    @display(description=_('Store'))
    def display_store_header(self, instance: Attendance):
        """
        Muestra el nombre de la tienda.
        """
        return instance.store.full_name
    
    @display(
        description=_('Autimatic'),
        label={
            _('no'): 'danger',
            _('yes'): 'success',
        },
        boolean=True
    )
    def display_autimatic_header(self, instance: Attendance):
        return _('yes') if instance.automatic else _('no')

    @display(description=_('Created'))
    def display_created(self, instance: Attendance):
        return instance.created_at