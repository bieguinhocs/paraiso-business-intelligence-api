from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm 
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    add_fieldsets = (
        (
            _('Personal info'), 
            {
                'fields': (
                    (
                        'document_type',
                        'document_number',
                    ),
                    (
                        'first_name',
                        'last_name',
                    ),
                    'supervisor',
                ),
                'classes': ('wide',),
            },
        ),
        (
            _('Credentials'),
            {
                'fields': (
                    'username',
                    'password1',
                    'password2',
                ),
                'classes': ('wide',),
            }
        ),
    )
    list_display = (
        'display_username',
        'display_name',
        'display_document_type',
        'display_document_number',
        'display_status',
        'display_staff',
        'display_superuser',
        'display_created',
    )
    search_fields = (
        'username',
        'document_number',
        'first_name',
        'last_name'
    )
    fieldsets = (
        (
            _('Access and security'),
            {
                'fields': (
                    'username',
                    'password',
                    'last_login',
                ),
            },
        ),
        (
            _('Personal info'),
            {
                'fields': (
                    (
                        'document_type',
                        'document_number',
                    ),
                    (
                        'first_name',
                        'last_name',
                    ),
                    'email',
                    (
                        'corporate_phone',
                        'corporate_device_imei',
                    ),
                    'supervisor',
                ),
                'classes': ['tab',],
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
                'classes': ['tab',],
            },
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'employment_start_date',
                    'employment_end_date',
                    'created_at',
                ),
                'classes': ['tab',],
            },
        ),
    )
    autocomplete_fields = (
        'supervisor',
    )
    radio_fields = {
        'document_type': admin.VERTICAL,
    }
    readonly_fields = (
        'last_login',
        'created_at',
    )

    @display(description=_('User'))
    def display_username(self, instance: User):
        return instance.username
    
    @display(description=_('Name'))
    def display_name(self, instance: User):
        return instance.full_name
    
    @display(description=_('Document type'), label=True)
    def display_document_type(self, instance: User):
        return instance.document_type
    
    @display(description=_('Document No.'))
    def display_document_number(self, instance: User):
        return instance.document_number
    
    @display(
        description=_('Status'),
        label={
            _('inactive'): 'danger',
            _('active'): 'success',
        },
    )
    def display_status(self, instance: User):
        return _('active') if instance.is_active else _('inactive')
    
    @display(
        description=_('Staff'),
        label={
            _('no'): 'danger',
            _('yes'): 'success',
        },
        boolean=True
    )
    def display_staff(self, instance: User):
        return _('yes') if instance.is_staff else _('no')

    @display(
        description=_('Superuser'),
        label={
            _('no'): 'danger',
            _('yes'): 'success',
        },
        boolean=True
    )
    def display_superuser(self, instance: User):
        return _('yes') if instance.is_superuser else _('no')

    @display(description=_('Created'))
    def display_created(self, instance: User):
        return instance.created_at
   
@admin.register(Group)
class GroupAdmin(GroupAdmin, ModelAdmin):
    fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    'name',
                    'permissions',
                ),
            },
        ),
    )