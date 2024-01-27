from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.Serializer):
    phone = serializers.CharField()

    class Meta:
        fields = ["phone"]


class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)
    code = serializers.IntegerField(required=True)

    class Meta:
        fields = ['phone', 'code']


class UpdateFullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True,
        error_messages={"min_length": "Не менее 8 символов."},
    )
    class Meta:
        model = User
        fields = ['phone', 'password']
