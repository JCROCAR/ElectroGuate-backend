# Django REST Framework
from rest_framework.mixins import DestroyModelMixin
# Utilities
from django.utils import timezone

class SoftDestroyModelMixin(DestroyModelMixin):
    """
    Update the registry as voided so as not to delete it from the database.
    """
    def soft_delete(self, instance):
        instance.is_deleted = True
        instance.deleted_at = timezone.now()
        instance.save()
