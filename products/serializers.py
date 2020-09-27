from rest_framework import serializers
from products.models import Product

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
            'int_price',
            'category_id']
