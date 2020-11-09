from pyasn1.type.univ import Null
from rest_framework import serializers
from .models import Product, Category, Brand

class ImageSerializer(serializers.Serializer):
    url_image = serializers.CharField()
    
    class Meta:
        fields=[
            "url_image"
        ]

class CategorySerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in Category
    """
    url_image = serializers.CharField()

    class Meta:
        model = Category
        fields = [
            "id",
            "str_name",
            "str_description",
            "url_image",
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
            "url_image",
        ]

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for product
    """
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = [
            "id",
            "str_name",
            "str_description",
            "str_product_code",
            "int_amount",
            "int_price",
            "category",
            "brand",
            "images"
        ]

class ProductListSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)


class BrandSerializerWrite(serializers.ModelSerializer):
    url_image = serializers.CharField()
    class Meta:
        model = Brand
        fields = [
            "id",
            "str_name",
            "str_description",
            "url_image",
            "category",
        ]

class BrandSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "str_name",
            "str_description",
            "url_image",
        ]