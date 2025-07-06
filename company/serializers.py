from rest_framework import serializers
from company.models import Company

class CompanyContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        read_only_fields = [fields]

