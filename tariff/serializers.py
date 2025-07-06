from rest_framework import serializers
from .models import TariffPlan

class TariffPlanSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = TariffPlan
        fields = '__all__'

    def get_discounted_price(self, obj):
        return obj.discounted_price()
