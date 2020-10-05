from rest_framework import serializers
from .models import Product, Category, Brand


class CategorySerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in Category
    """

    class Meta:
        model = Category
        fields = [
            "str_name",
            "str_description",
            "str_image_link",
        ]


class CategorySerializerRead(serializers.ModelSerializer):
    """
    Serializer to read data in Category
    """

    class Meta:
        model = Category
        fields = [
            "id",
            "str_name",
            "str_description",
            "str_image_link",
        ]


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for product
    """

    class Meta:
        model = Product
        fields = [
            "id",
            "str_name",
            "str_description",
            "str_product_code",
            "str_image_link",
            "int_amount",
            "int_price",
            "category",
            "brand",
        ]


class BrandSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "str_name",
            "str_description",
            "str_image_link",
            "category",
        ]


class BrandSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "str_name",
            "str_description",
            "str_image_link",
        ]
