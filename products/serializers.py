from rest_framework import serializers
from .models import Product, Category

"""
Serializer for product
"""


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'str_name',
            'str_description',
            'str_product_code',
            'str_image_link',
            'int_amount',
            'int_price',]


class CategorySerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in Category
    """
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializerRead(serializers.ModelSerializer):
    """
    Serializer to read data in Category
    """
    class Meta:
        model=Category
        fields = [
            'id',
            'str_name',
            'str_description',
            'str_image_link',
        ]
