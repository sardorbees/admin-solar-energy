from rest_framework import generics
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('search', '').strip()

        if query:
            return Product.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(slug__icontains=query)
            ).distinct().order_by('-id')  # последние товары выше
        return Product.objects.all().order_by('-id')
