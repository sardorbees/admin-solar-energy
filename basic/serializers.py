from rest_framework import serializers
from .models import ClickTransaction

class ClickTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickTransaction
        fields = '__all__'
        ref_name = 'ProductClikckjbdsf'
