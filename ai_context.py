"""
AI context for the Quality module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Quality

### Models

**Inspection**
- `reference` (str, required), `title` (str, required)
- `inspection_type` (str, default 'incoming') — free text, common values: incoming, in_process, final, audit
- `status` choices: pending | in_progress | passed | failed (default: pending)
- `inspector_id` (UUID, optional — references a LocalUser), `inspection_date` (date, optional)
- `result` (str, default 'pending') — stores the final outcome text or code
- `notes` (text)

### Key Flows

1. **Create inspection**: set reference and title, choose inspection_type (e.g. 'incoming' for goods received, 'final' before shipping).
2. **Assign inspector**: set inspector_id (UUID of the responsible user).
3. **Conduct inspection**: update status to 'in_progress', fill inspection_date.
4. **Record outcome**: set status to 'passed' or 'failed' and update result field with details. Add notes for context.

### Relationships

- `inspector_id` is a raw UUID field (no FK) — maps to LocalUser in the accounts module.
- No direct FK to manufacturing batches or inventory in this module; use reference field to link externally.
- Manufacturing's ProductionBatch has its own `quality_status` field — the Quality module provides standalone inspection records that can complement it.
"""
