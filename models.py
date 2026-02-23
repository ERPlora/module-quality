from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

INSP_STATUS = [
    ('pending', _('Pending')),
    ('in_progress', _('In Progress')),
    ('passed', _('Passed')),
    ('failed', _('Failed')),
]

class Inspection(HubBaseModel):
    reference = models.CharField(max_length=50, verbose_name=_('Reference'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    inspection_type = models.CharField(max_length=30, default='incoming', verbose_name=_('Inspection Type'))
    status = models.CharField(max_length=20, default='pending', choices=INSP_STATUS, verbose_name=_('Status'))
    inspector_id = models.UUIDField(null=True, blank=True, verbose_name=_('Inspector Id'))
    inspection_date = models.DateField(null=True, blank=True, verbose_name=_('Inspection Date'))
    result = models.CharField(max_length=20, default='pending', verbose_name=_('Result'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'quality_inspection'

    def __str__(self):
        return self.title

