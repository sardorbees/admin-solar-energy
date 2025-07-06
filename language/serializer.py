from rest_framework import serializers
from language.models import Language

class LanguageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
        read_only_fields = [fields]