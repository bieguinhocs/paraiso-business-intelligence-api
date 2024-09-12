import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_ruc(ruc):
    """
    Valida que el RUC contenga exactamente 11 dígitos.
    """
    if not ruc.isdigit():
        raise ValidationError(_('The RUC must contain only digits.'))
    if len(ruc) != 11:
        raise ValidationError(_('The RUC must have exactly 11 digits.'))

def validate_alpha_numeric_code(code):
    """
    Valida y formatea un código. El formato debe consistir en 3 letras seguidas de 3 números.
    """
    # Verifica que el código siga el formato de 3 letras seguidas de 3 números
    match = re.match(r"^([a-zA-Z]{3})(\d{3})$", code)
    if not match:
        # Si el formato no coincide, lanza un error de validación
        raise ValidationError(_('The code must consist of exactly 3 letters followed by 3 numbers.'))
