from rest_framework import serializers
from .models import Rental
from rest_framework import serializers


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ["poit_a", "poit_b", "total_cost", "payment_type"]


class CallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ["id", "passenger", "poit_a", "poit_b", "total_cost", "payment_type"]


class AcceptCallSerializer(serializers.ModelSerializer):
    call_id = serializers.IntegerField()

    class Meta:
        model = Rental
        fields = ['call_id']