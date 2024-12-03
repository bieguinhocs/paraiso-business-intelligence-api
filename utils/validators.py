from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_only_digits(value):
    """
    Valida que el valor contenga únicamente dígitos.
    """
    if not value.isdigit():
        raise ValidationError(_('This field must contain only digits.'))

def validate_document_number(document_number, document_type):
    """
    Valida el número de documento según el tipo (DNI o CE).
    """
    if not document_number.isdigit():
        raise ValidationError(_('The document number must contain only digits.'))

    if document_type == 'DNI' and len(document_number) != 8:
        raise ValidationError(_('Document number must be exactly 8 digits for DNI.'))
    elif document_type == 'CE' and len(document_number) != 9:
        raise ValidationError(_('Document number must be exactly 9 digits for foreigner card.'))
