from rest_framework import serializers
from category_title.models import CategoryTitle

class CategoryTitleTextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTitle
        fields = "__all__"
        read_only_fields = [fields]

