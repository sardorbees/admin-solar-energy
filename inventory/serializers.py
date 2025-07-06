# inventory/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        ref_name = 'ProductTitleList'
        
    def get_can_buy_now(self, obj):
        return obj.stock

    def get_purchased_this_week(self, obj):
        week_ago = now() - timedelta(days=7)
        return Purchase.objects.filter(product=obj, created_at__gte=week_ago).count()

    def get_remaining_stock(self, obj):
        return obj.stock - Purchase.objects.filter(product=obj).aggregate(
            total=models.Sum('quantity'))['total'] or 0
