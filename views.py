"""
Quality Control Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('quality', 'dashboard')
@htmx_view('quality/pages/dashboard.html', 'quality/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('quality', 'inspections')
@htmx_view('quality/pages/inspections.html', 'quality/partials/inspections_content.html')
def inspections(request):
    """Inspections view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('quality', 'settings')
@htmx_view('quality/pages/settings.html', 'quality/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

