# serializers/favorite_serializer.py
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        slug_field='model',
        queryset=ContentType.objects.all()
    )

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'content_type', 'object_id', 'added_at']
        read_only_fields = ['id', 'added_at']
