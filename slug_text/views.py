from rest_framework import viewsets
from .models import SlugCategory
from .serializers import SlugCategorySerializer

class SlugCategoryViewSet(viewsets.ModelViewSet):
    queryset = SlugCategory.objects.all()
    serializer_class = SlugCategorySerializer