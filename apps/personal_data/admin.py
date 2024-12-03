from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import PersonalData
from unfold.decorators import display
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static
from django.utils.html import format_html

@admin.register(PersonalData)
class PersonalDataAdmin(ModelAdmin):
    add_fieldsets = (
        (
            _('Overview'),
            {
                'fields': (
                    ('client_first_name', 'client_last_name'),
                    ('client_document_type', 'client_document_number'),
                    ('client_phone', 'client_email'),
                    ('answer_1', 'answer_2'),
                    'photo',
                    ('sale',),
                ),
                'classes': ('wide',),
            },
        ),
    )
    list_display = (
        'display_client_survey',
        'client_phone',
        'client_email',
        'display_created',
    )
    search_fields = (
        'client_first_name',
        'client_last_name',
        'client_document_number',
        'client_email',
        'sale__id',
    )
    list_filter = (
        'client_document_type',
        'created_at',
    )
    fieldsets = (
        (
            _('Personal Information'),
            {
                'fields': (
                    ('client_first_name', 'client_last_name'),
                    ('client_document_type', 'client_document_number'),
                ),
                'classes': ['tab'],
            },
        ),
        (
            _('Contact Details'),
            {
                'fields': (
                    ('client_phone', 'client_email'),
                ),
                'classes': ['tab'],
            },
        ),
        (
            _('Additional Information'),
            {
                'fields': (
                    ('answer_1', 'answer_2'),
                    'photo_preview',
                ),
                'classes': ['tab'],
            },
        ),
        (
            _('Related Sale'),
            {
                'fields': (
                    'sale',
                ),
                'classes': ['tab'],
            },
        ),
        (
            _('Important Dates'),
            {
                'fields': (
                    'created_at',
                ),
                'classes': ['tab'],
            },
        ),
    )
    radio_fields = {
        'client_document_type': admin.HORIZONTAL,
    }
    autocomplete_fields = (
        'sale',
    )
    readonly_fields = (
        'photo_preview',
        'created_at',
    )

    @display(description=_('Survey'), header=True)
    def display_client_survey(self, instance: PersonalData):
        """
        Muestra datos y foto de la encuesta al cliente.
        """
        return [
            f"{instance.client_first_name} {instance.client_last_name}",
            instance.client_document_number,
            None,
            {
                "path": instance.photo.url,
                "squared": False,
                "borderless": True,
            },
        ]

    @display(description=_('Created'))
    def display_created(self, instance: PersonalData):
        return instance.created_at
    
    def photo_preview(self, obj):
        if obj.photo:
            # Renderiza una vista previa de la imagen con un enlace para descargarla
            return format_html(
                '<div style="display: flex; justify-content: center; align-items: center; height: 100%; width: 100%;">'
                '    <a href="{}" target="_blank">'
                '        <img src="{}" alt="{}" style="max-height: 100%; max-width: 100%; object-fit: contain; border-radius: 5px;" />'
                '    </a>'
                '</div>',
                obj.photo.url,
                obj.photo.url,
                'Photo Preview'
            )
        return _('No photo available')
    photo_preview.short_description = 'Photo'