# Quality Control

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `quality` |
| **Version** | `1.0.0` |
| **Icon** | `shield-checkmark-outline` |
| **Dependencies** | None |

## Models

### `Inspection`

Inspection(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, reference, title, inspection_type, status, inspector_id, inspection_date, result, notes)

| Field | Type | Details |
|-------|------|---------|
| `reference` | CharField | max_length=50 |
| `title` | CharField | max_length=255 |
| `inspection_type` | CharField | max_length=30 |
| `status` | CharField | max_length=20, choices: pending, in_progress, passed, failed |
| `inspector_id` | UUIDField | max_length=32, optional |
| `inspection_date` | DateField | optional |
| `result` | CharField | max_length=20 |
| `notes` | TextField | optional |

## URL Endpoints

Base path: `/m/quality/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `inspections/` | `inspections_list` | GET |
| `inspections/add/` | `inspection_add` | GET/POST |
| `inspections/<uuid:pk>/edit/` | `inspection_edit` | GET |
| `inspections/<uuid:pk>/delete/` | `inspection_delete` | GET/POST |
| `inspections/bulk/` | `inspections_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `quality.view_inspection` | View Inspection |
| `quality.add_inspection` | Add Inspection |
| `quality.change_inspection` | Change Inspection |
| `quality.delete_inspection` | Delete Inspection |
| `quality.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_inspection`, `change_inspection`, `view_inspection`
- **employee**: `add_inspection`, `view_inspection`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Inspections | `shield-checkmark-outline` | `inspections` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_inspections`

List quality inspections.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | pending, in_progress, passed, failed |
| `inspection_type` | string | No |  |
| `limit` | integer | No |  |

### `create_inspection`

Create a quality inspection.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes |  |
| `inspection_type` | string | Yes | incoming, in_process, final, etc. |
| `inspection_date` | string | No |  |
| `notes` | string | No |  |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  icons/
    icon.svg
  quality/
    css/
    js/
templates/
  quality/
    pages/
      dashboard.html
      index.html
      inspection_add.html
      inspection_edit.html
      inspections.html
      settings.html
    partials/
      dashboard_content.html
      inspection_add_content.html
      inspection_edit_content.html
      inspections_content.html
      inspections_list.html
      panel_inspection_add.html
      panel_inspection_edit.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
