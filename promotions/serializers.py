# promotions/serializers.py
from rest_framework import serializers
from .models import Promotion

class PromotionSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Promotion
        fields = ['id', 'product', 'product_name', 'title', 'discount_percent', 'start_date', 'end_date', 'is_active']
