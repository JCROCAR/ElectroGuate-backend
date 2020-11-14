from rest_framework import serializers
from .models import Order, DetailOrder
from users.serializers import UserSerializerRead
from products.serializers import ProductSerializer

class OrderSerializerRead(serializers.ModelSerializer):
    """
    Serializer to read data from Order
    """
    user = UserSerializerRead(many=False)
    class Meta:
        model = Order
        fields = (
            'id',
            'created_at',
            'user',
            'str_deposit_number',
            'total'
        )

class OrderSerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in Order.
    """
    class Meta:
        model = Order
        fields = '__all__'


class DetailOrderSerializerRead(serializers.ModelSerializer):
    """
    Serializer to read data from DetailOrder
    """
    product = ProductSerializer(many=False)
    order = OrderSerializerRead(many=False)
    class Meta:
        model = DetailOrder
        fields = (
            'id',
            'product',
            'order',
            'amount',
            'price'
        )

class DetailOrderSerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in DetailOrder
    """
    class Meta:
        model = DetailOrder
        fields = '__all__'