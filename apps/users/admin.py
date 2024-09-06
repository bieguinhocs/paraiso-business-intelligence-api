from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm 
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display
from django.templatetags.static import static
from stores.models import Store
from unfold.admin import ModelAdmin, StackedInline, TabularInline

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

class StoreInline(TabularInline):
    model = Store
    fields = ['code', 'name', 'retail', 'is_covered']
    readonly_fields = ['code', 'name', 'retail',]
    show_change_link = True
    can_delete = True
    tab = True
    max_num = 0
    extra = 0

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    inlines = [StoreInline,]
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
                    'coordinator',
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
        'display_user',
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
                    'address',
                    'coordinator',
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
        'address',
        'coordinator',
    )
    radio_fields = {
        'document_type': admin.VERTICAL,
    }
    readonly_fields = (
        'last_login',
        'created_at',
    )
    
    @display(description=_('Username'))
    def display_username(self, instance: User):
        return instance.username

    @display(description=_('User'), header=True)
    def display_user(self, instance: User):
        """
        Muestra el nombre completo en la primera línea,los roles en la segunda,
        y un avatar en un círculo.
        """
        return [
            instance.full_name,
            instance.groups_list,
            None,
            {
                "path": static("images/avatar.jpg"),
                "squared": False,
                "borderless": True,
            }
        ]
    
    @display(description=_('Document'), label=True)
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
    
    def get_search_results(self, request, queryset, search_term):
        # Verifica si la búsqueda de autocompletar es para el campo 'coordinator'
        if request.GET.get('field_name') == 'coordinator':
            queryset, use_distinct = super().get_search_results(request, queryset, search_term)
            # Filtra los usuarios que pertenecen al grupo 'Coordinador' y están activos
            coordinador_group = Group.objects.get(name='Coordinador')
            queryset = queryset.filter(groups=coordinador_group, is_active=True)
            return queryset, use_distinct
        
        # Verifica si la búsqueda de autocompletar es para el campo 'promoters'
        if request.GET.get('field_name') == 'promoters':
            queryset, use_distinct = super().get_search_results(request, queryset, search_term)
            # Filtra los usuarios que pertenecen al grupo 'Promotor' y están activos
            promoter_group = Group.objects.get(name='Promotor')
            queryset = queryset.filter(groups=promoter_group, is_active=True)
            return queryset, use_distinct

        # Comportamiento predeterminado para otros campos
        return super().get_search_results(request, queryset, search_term)

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