"""Tests for quality views."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestDashboard:
    """Dashboard view tests."""

    def test_dashboard_loads(self, auth_client):
        """Test dashboard page loads."""
        url = reverse('quality:dashboard')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_dashboard_htmx(self, auth_client):
        """Test dashboard HTMX partial."""
        url = reverse('quality:dashboard')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_dashboard_requires_auth(self, client):
        """Test dashboard requires authentication."""
        url = reverse('quality:dashboard')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestInspectionViews:
    """Inspection view tests."""

    def test_list_loads(self, auth_client):
        """Test list view loads."""
        url = reverse('quality:inspections_list')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_list_htmx(self, auth_client):
        """Test list HTMX partial."""
        url = reverse('quality:inspections_list')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_list_search(self, auth_client):
        """Test list search."""
        url = reverse('quality:inspections_list')
        response = auth_client.get(url, {'q': 'test'})
        assert response.status_code == 200

    def test_list_sort(self, auth_client):
        """Test list sorting."""
        url = reverse('quality:inspections_list')
        response = auth_client.get(url, {'sort': 'created_at', 'dir': 'desc'})
        assert response.status_code == 200

    def test_export_csv(self, auth_client):
        """Test CSV export."""
        url = reverse('quality:inspections_list')
        response = auth_client.get(url, {'export': 'csv'})
        assert response.status_code == 200
        assert 'text/csv' in response['Content-Type']

    def test_export_excel(self, auth_client):
        """Test Excel export."""
        url = reverse('quality:inspections_list')
        response = auth_client.get(url, {'export': 'excel'})
        assert response.status_code == 200

    def test_add_form_loads(self, auth_client):
        """Test add form loads."""
        url = reverse('quality:inspection_add')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_add_post(self, auth_client):
        """Test creating via POST."""
        url = reverse('quality:inspection_add')
        data = {
            'reference': 'New Reference',
            'title': 'New Title',
            'inspection_type': 'New Inspection Type',
            'status': 'New Status',
            'inspector_id': 'test',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_edit_form_loads(self, auth_client, inspection):
        """Test edit form loads."""
        url = reverse('quality:inspection_edit', args=[inspection.pk])
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_edit_post(self, auth_client, inspection):
        """Test editing via POST."""
        url = reverse('quality:inspection_edit', args=[inspection.pk])
        data = {
            'reference': 'Updated Reference',
            'title': 'Updated Title',
            'inspection_type': 'Updated Inspection Type',
            'status': 'Updated Status',
            'inspector_id': 'test',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_delete(self, auth_client, inspection):
        """Test soft delete via POST."""
        url = reverse('quality:inspection_delete', args=[inspection.pk])
        response = auth_client.post(url)
        assert response.status_code == 200
        inspection.refresh_from_db()
        assert inspection.is_deleted is True

    def test_bulk_delete(self, auth_client, inspection):
        """Test bulk delete."""
        url = reverse('quality:inspections_bulk_action')
        response = auth_client.post(url, {'ids': str(inspection.pk), 'action': 'delete'})
        assert response.status_code == 200
        inspection.refresh_from_db()
        assert inspection.is_deleted is True

    def test_list_requires_auth(self, client):
        """Test list requires authentication."""
        url = reverse('quality:inspections_list')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestSettings:
    """Settings view tests."""

    def test_settings_loads(self, auth_client):
        """Test settings page loads."""
        url = reverse('quality:settings')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_settings_requires_auth(self, client):
        """Test settings requires authentication."""
        url = reverse('quality:settings')
        response = client.get(url)
        assert response.status_code == 302

