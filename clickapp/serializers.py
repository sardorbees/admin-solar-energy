# security/serializers.py
from rest_framework import serializers
from .models import SuspiciousUser

class SuspiciousUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspiciousUser
        fields = "__all__"
