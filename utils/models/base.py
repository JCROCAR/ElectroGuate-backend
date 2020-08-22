"""
Ferry base models.
"""
# Django
from django.db import models

class BaseModel(models.Model):
    """
    Ferry base model.

    FerryBaseModel acts as an abstract base class from which another project model
    will inherit. This class provides each model with the following attributes:
        + is_deleted  (Boolean):  Store whether or not the object is deleted.
        + deleted_at  (DateTime): Store the date and time the object was deleted
        + created_at  (DateTime): Store the last datetime the object was modified.
        + modified_at (DateTime): Store the datetime the object was created.
    """
    is_deleted = models.BooleanField(
        'is deleted',
        default=False,
        help_text='Indicates whether or not the object is deleted.'
    )
    deleted_at = models.DateTimeField(
        'deleted at',
        null=True,
        help_text='Date and time the object was deleted.'
    )
    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date and time the object was created.'
    )
    modified_at = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date and time the object was last modified.'
    )

    class Meta:
        """
        Meta option.
        """
        abstract = True