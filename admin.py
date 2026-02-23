from django.contrib import admin

from .models import Inspection

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ['reference', 'title', 'inspection_type', 'status', 'inspector_id']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']

