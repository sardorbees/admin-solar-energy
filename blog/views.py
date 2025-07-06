from rest_framework import generics
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = PostListSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
