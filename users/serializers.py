from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializerRead(serializers.ModelSerializer):
    """
    Serializer to read data from User.
    """
    class Meta:
        model = User
        fields = (
            'id',
            'str_name',
            'str_surname',
            'str_role',
            'str_phone_number',
        )

class UserSerializerWrite(serializers.ModelSerializer):
    """
    Serializer to write data in User.
    """
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User(**validated_data)
        print(validated_data)
        print(validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user