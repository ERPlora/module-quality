    from django.utils.translation import gettext_lazy as _

    MODULE_ID = 'quality'
    MODULE_NAME = _('Quality Control')
    MODULE_VERSION = '1.0.0'
    MODULE_ICON = 'shield-checkmark-outline'
    MODULE_DESCRIPTION = _('Quality inspections, checklists and non-conformance tracking')
    MODULE_AUTHOR = 'ERPlora'
    MODULE_CATEGORY = 'operations'

    MENU = {
        'label': _('Quality Control'),
        'icon': 'shield-checkmark-outline',
        'order': 59,
    }

    NAVIGATION = [
        {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Inspections'), 'icon': 'shield-checkmark-outline', 'id': 'inspections'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
    ]

    DEPENDENCIES = []

    PERMISSIONS = [
        'quality.view_inspection',
'quality.add_inspection',
'quality.change_inspection',
'quality.delete_inspection',
'quality.manage_settings',
    ]
