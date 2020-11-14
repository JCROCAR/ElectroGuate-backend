from django.db import models
from utils.models.base import BaseModel
from django.utils.translation import gettext_lazy as _


class Category(BaseModel):
    """
    Create a Category
    """

    str_name = models.CharField(max_length=45)
    str_description = models.CharField(max_length=45)
    url_image = models.URLField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.str_name


class Brand(BaseModel):
    """
    Create a Brand
    """

    str_name = models.CharField(max_length=45)
    str_description = models.CharField(max_length=45)
    url_image = models.URLField(max_length=250, blank=True, null=True)
    category = models.ForeignKey(
        Category, default=1, related_name="brands", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.str_name


class Product(models.Model):
    """
    Create a product
    """

    str_name = models.CharField(max_length=45, blank=False)
    str_description = models.TextField(default="")
    str_product_code = models.CharField(max_length=45, blank=False)
    int_amount = models.IntegerField(blank=False)
    int_price = models.FloatField(blank=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1,
        related_name="products",
        blank=False,
    )
    brand = models.ForeignKey(
        Brand, default=1, related_name="products", on_delete=models.CASCADE, blank=False
    )

    def __str__(self):
        return self.str_name


class Image(models.Model):
    url_image = models.URLField(max_length=250, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self):
        return self.url_image