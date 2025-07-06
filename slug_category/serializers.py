from rest_framework import serializers
from .models import SlugCategory

class SlugCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SlugCategory
        fields = '__all__'