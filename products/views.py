# products/views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
