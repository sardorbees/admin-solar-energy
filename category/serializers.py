from rest_framework import serializers
from category.models import Category

class CategoryPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = [fields]

