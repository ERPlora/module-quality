# Quality Control Module

Quality inspections, checklists and non-conformance tracking.

## Features

- Create and manage quality inspections with full status tracking (pending, in progress, passed, failed)
- Assign inspectors to inspections
- Classify inspections by type (e.g., incoming, in-process, final)
- Record inspection dates and results
- Add notes and observations to each inspection

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Quality Control > Settings**

## Usage

Access via: **Menu > Quality Control**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/quality/dashboard/` | Overview of inspection activity and results |
| Inspections | `/m/quality/inspections/` | List and manage quality inspections |
| Settings | `/m/quality/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `Inspection` | Quality inspection with reference, title, type, status, inspector, date, result, and notes |

## Permissions

| Permission | Description |
|------------|-------------|
| `quality.view_inspection` | View inspections |
| `quality.add_inspection` | Create new inspections |
| `quality.change_inspection` | Edit existing inspections |
| `quality.delete_inspection` | Delete inspections |
| `quality.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
