from rest_framework import serializers

from users.serializers import UserSerializerRead
from orders.serializers import OrderSerializerRead
from .models import Payment

class PaymentSerializerRead(serializers.ModelSerializer):
    """
    Serializer to read data from a Payment
    """
    user = UserSerializerRead(many=False)
    order = OrderSerializerRead(many=False)
    class Meta:
        model = Payment
        fields = (
            'id',
            'created_at',
            'user',
            'order',
            'str_card_number',
            'str_name',
            'card_date'
        )

class PaymentSerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in Payment.
    """
    class Meta:
        model = Payment
        fields = '__all__'
