from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Показываем username

    class Meta:
        model = ChatMessage
        fields = ['id', 'user', 'message', 'is_bot', 'timestamp']
