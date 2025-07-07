from rest_framework import serializers
from .models import ClickBlock

class ClickBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickBlock
        fields = '__all__'
