from rest_framework import serializers
from category_servicess.models import CategoryTitle

class CategoryTitleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTitle
        fields = "__all__"
        read_only_fields = [fields]
        ref_name = 'CategorySerss'

