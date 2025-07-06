# gallery/views.py
from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer

class ImageListAPIView(generics.ListAPIView):
    queryset = Image.objects.all().order_by('-created_at')
    serializer_class = ImageSerializer
