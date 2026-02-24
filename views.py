"""
Quality Control Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import Inspection

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('quality', 'dashboard')
@htmx_view('quality/pages/index.html', 'quality/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_inspections': Inspection.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# Inspection
# ======================================================================

INSPECTION_SORT_FIELDS = {
    'title': 'title',
    'reference': 'reference',
    'status': 'status',
    'inspection_type': 'inspection_type',
    'inspector_id': 'inspector_id',
    'inspection_date': 'inspection_date',
    'created_at': 'created_at',
}

def _build_inspections_context(hub_id, per_page=10):
    qs = Inspection.objects.filter(hub_id=hub_id, is_deleted=False).order_by('title')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'inspections': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'title',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_inspections_list(request, hub_id, per_page=10):
    ctx = _build_inspections_context(hub_id, per_page)
    return django_render(request, 'quality/partials/inspections_list.html', ctx)

@login_required
@with_module_nav('quality', 'inspections')
@htmx_view('quality/pages/inspections.html', 'quality/partials/inspections_content.html')
def inspections_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'title')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = Inspection.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(reference__icontains=search_query) | Q(title__icontains=search_query) | Q(inspection_type__icontains=search_query) | Q(status__icontains=search_query))

    order_by = INSPECTION_SORT_FIELDS.get(sort_field, 'title')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['title', 'reference', 'status', 'inspection_type', 'inspector_id', 'inspection_date']
        headers = ['Title', 'Reference', 'Status', 'Inspection Type', 'Inspector Id', 'Inspection Date']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='inspections.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='inspections.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'quality/partials/inspections_list.html', {
            'inspections': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'inspections': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
def inspection_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        reference = request.POST.get('reference', '').strip()
        title = request.POST.get('title', '').strip()
        inspection_type = request.POST.get('inspection_type', '').strip()
        status = request.POST.get('status', '').strip()
        inspector_id = request.POST.get('inspector_id', '').strip()
        inspection_date = request.POST.get('inspection_date') or None
        result = request.POST.get('result', '').strip()
        notes = request.POST.get('notes', '').strip()
        obj = Inspection(hub_id=hub_id)
        obj.reference = reference
        obj.title = title
        obj.inspection_type = inspection_type
        obj.status = status
        obj.inspector_id = inspector_id
        obj.inspection_date = inspection_date
        obj.result = result
        obj.notes = notes
        obj.save()
        return _render_inspections_list(request, hub_id)
    return django_render(request, 'quality/partials/panel_inspection_add.html', {})

@login_required
def inspection_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Inspection, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.reference = request.POST.get('reference', '').strip()
        obj.title = request.POST.get('title', '').strip()
        obj.inspection_type = request.POST.get('inspection_type', '').strip()
        obj.status = request.POST.get('status', '').strip()
        obj.inspector_id = request.POST.get('inspector_id', '').strip()
        obj.inspection_date = request.POST.get('inspection_date') or None
        obj.result = request.POST.get('result', '').strip()
        obj.notes = request.POST.get('notes', '').strip()
        obj.save()
        return _render_inspections_list(request, hub_id)
    return django_render(request, 'quality/partials/panel_inspection_edit.html', {'obj': obj})

@login_required
@require_POST
def inspection_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Inspection, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_inspections_list(request, hub_id)

@login_required
@require_POST
def inspections_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = Inspection.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_inspections_list(request, hub_id)


@login_required
@with_module_nav('quality', 'settings')
@htmx_view('quality/pages/settings.html', 'quality/partials/settings_content.html')
def settings_view(request):
    return {}

