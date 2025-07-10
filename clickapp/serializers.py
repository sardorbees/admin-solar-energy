from rest_framework import serializers
from .models import VisitorClick

class VisitorClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorClick
        fields = '__all__'
