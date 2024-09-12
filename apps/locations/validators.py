from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def validate_latitude(latitude):
    if not (-90 <= latitude <= 90):
        raise ValidationError(_('Latitude must be between -90 and 90 degrees.'))

def validate_longitude(longitude):
    if not (-180 <= longitude <= 180):
        raise ValidationError(_('Longitude must be between -180 and 180 degrees.'))