import os
import sys
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.utils import timezone
from utils.mixins import SoftDestroyModelMixin
from utils.models.base import BaseModel
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(BaseModel):
    """
    Upload image
    """

    def upload_to(instance, filename):
        now = timezone.now()
        base, extension = os.path.splitext(filename.lower())
        milliseconds = now.microsecond // 1000
        return f"users/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

    """
    Create a Category
    """
    str_name = models.CharField(
        max_length=45,
    )
    str_description = models.CharField(
        max_length=45,
    )
    str_image_link = models.ImageField(
        upload_to=upload_to,
        null=True,
    )


class Brand(BaseModel):
    """
    Upload image
    """

    def upload_to(instance, filename):
        now = timezone.now()
        base, extension = os.path.splitext(filename.lower())
        milliseconds = now.microsecond // 1000
        return f"users/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

    """
    Create a Brand
    """
    str_name = models.CharField(
        max_length=45,
    )
    str_description = models.CharField(
        max_length=45,
    )
    str_image_link = models.ImageField(
        upload_to=upload_to,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        default=1,
        related_name="brands",
        on_delete=models.CASCADE,
    )


class Product(models.Model):
    """
    Upload image
    """

    def upload_to(instance, filename):
        now = timezone.now()
        base, extension = os.path.splitext(filename.lower())
        milliseconds = now.microsecond // 1000
        return f"users/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

    """
    Create a product
    """
    str_name = models.CharField(
        max_length=45,
        blank=False,
    )
    str_description = models.CharField(
        max_length=45,
        default="",
        blank=True,
    )
    str_product_code = models.CharField(
        max_length=45,
        blank=False,
    )
    str_image_link = models.ImageField(
        _("Product_image"),
        upload_to=upload_to,
        null=True,
    )
    int_amount = models.IntegerField(
        blank=False,
    )
    int_price = models.FloatField(
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1,
        related_name="products",
        blank=False,
    )
    brand = models.ForeignKey(
        Brand,
        default=1,
        related_name="products",
        on_delete=models.CASCADE,
        blank=False,
    )
