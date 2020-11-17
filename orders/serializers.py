from products.models import Product
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Order, DetailOrder
from users.serializers import UserSerializerRead
from products.serializers import ImageSerializer


class OrderSerializerRead(serializers.ModelSerializer):
    """
    Serializer to read data from Order
    """

    user = UserSerializerRead(many=False)

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user",
            "paypal_order_id",
            "total",
            "zip_code",
            "details",
        )


class OrderSerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in Order.
    """

    class Meta:
        model = Order
        fields = "__all__"


class DetailProducts(serializers.ModelSerializer):
    images=ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = [
            "str_name",
            "str_description",
            "str_product_code",
            "images"
        ]


class DetailOrderSerializerRead(serializers.ModelSerializer):
    """
    Serializer to read data from DetailOrder
    """

    product = DetailProducts(many=False)

    class Meta:
        model = DetailOrder
        fields = ("id", "product", "amount", "price")


class DetailOrderSerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in DetailOrder
    """

    class Meta:
        model = DetailOrder
        fields = "__all__"
