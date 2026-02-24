from django.urls import path
from . import views

app_name = 'quality'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Inspection
    path('inspections/', views.inspections_list, name='inspections_list'),
    path('inspections/add/', views.inspection_add, name='inspection_add'),
    path('inspections/<uuid:pk>/edit/', views.inspection_edit, name='inspection_edit'),
    path('inspections/<uuid:pk>/delete/', views.inspection_delete, name='inspection_delete'),
    path('inspections/bulk/', views.inspections_bulk_action, name='inspections_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
