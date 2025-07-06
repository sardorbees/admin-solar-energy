# comments/views.py
from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    parser_classes = [MultiPartParser, FormParser]
