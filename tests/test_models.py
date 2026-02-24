"""Tests for quality models."""
import pytest
from django.utils import timezone

from quality.models import Inspection


@pytest.mark.django_db
class TestInspection:
    """Inspection model tests."""

    def test_create(self, inspection):
        """Test Inspection creation."""
        assert inspection.pk is not None
        assert inspection.is_deleted is False

    def test_str(self, inspection):
        """Test string representation."""
        assert str(inspection) is not None
        assert len(str(inspection)) > 0

    def test_soft_delete(self, inspection):
        """Test soft delete."""
        pk = inspection.pk
        inspection.is_deleted = True
        inspection.deleted_at = timezone.now()
        inspection.save()
        assert not Inspection.objects.filter(pk=pk).exists()
        assert Inspection.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, inspection):
        """Test default queryset excludes deleted."""
        inspection.is_deleted = True
        inspection.deleted_at = timezone.now()
        inspection.save()
        assert Inspection.objects.filter(hub_id=hub_id).count() == 0


