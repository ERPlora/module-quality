from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QualityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quality'
    label = 'quality'
    verbose_name = _('Quality Control')

    def ready(self):
        pass
