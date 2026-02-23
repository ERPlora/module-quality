from django.urls import path
from . import views

app_name = 'quality'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('inspections/', views.inspections, name='inspections'),
    path('settings/', views.settings, name='settings'),
]
