from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet
from .admin import Category
from .serializers import CategoryPageContentSerializer


class CategoryPriceViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryPageContentSerializer