# serializers.py
from rest_framework import serializers
from .models import ClickPayment

class ClickPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickPayment
        fields = '__all__'
