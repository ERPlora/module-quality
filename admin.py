from django.contrib import admin

from .models import Inspection

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ['reference', 'title', 'inspection_type', 'status', 'inspector_id', 'created_at']
    search_fields = ['reference', 'title', 'inspection_type', 'status']
    readonly_fields = ['created_at', 'updated_at']

