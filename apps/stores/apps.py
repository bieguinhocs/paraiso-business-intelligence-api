from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class StoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stores'
    verbose_name = _('Stores')
