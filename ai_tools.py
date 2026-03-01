"""AI tools for the Quality module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListInspections(AssistantTool):
    name = "list_inspections"
    description = "List quality inspections."
    module_id = "quality"
    required_permission = "quality.view_inspection"
    parameters = {
        "type": "object",
        "properties": {
            "status": {"type": "string", "description": "pending, in_progress, passed, failed"},
            "inspection_type": {"type": "string"}, "limit": {"type": "integer"},
        },
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from quality.models import Inspection
        qs = Inspection.objects.all()
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        if args.get('inspection_type'):
            qs = qs.filter(inspection_type=args['inspection_type'])
        limit = args.get('limit', 20)
        return {"inspections": [{"id": str(i.id), "reference": i.reference, "title": i.title, "inspection_type": i.inspection_type, "status": i.status, "inspection_date": str(i.inspection_date) if i.inspection_date else None} for i in qs.order_by('-created_at')[:limit]]}


@register_tool
class CreateInspection(AssistantTool):
    name = "create_inspection"
    description = "Create a quality inspection."
    module_id = "quality"
    required_permission = "quality.add_inspection"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "title": {"type": "string"}, "inspection_type": {"type": "string", "description": "incoming, in_process, final, etc."},
            "inspection_date": {"type": "string"}, "notes": {"type": "string"},
        },
        "required": ["title", "inspection_type"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from quality.models import Inspection
        i = Inspection.objects.create(title=args['title'], inspection_type=args['inspection_type'], inspection_date=args.get('inspection_date'), notes=args.get('notes', ''))
        return {"id": str(i.id), "reference": i.reference, "created": True}
