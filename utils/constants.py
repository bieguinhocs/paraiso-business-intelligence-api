from django.utils.translation import gettext_lazy as _

DOCUMENT_TYPE_CHOICES = [
    ('DNI', _('Documento Nacional de Identidad')),
    ('CE', _('Carnet de Extranjería')),
]

YES_NO_CHOICES = [
    (1, _('Yes')),
    (0, _('No')),
]