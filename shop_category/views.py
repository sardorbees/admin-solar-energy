# products/views.py
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['power', 'category']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'rating', 'popularity']

    def get_queryset(self):
        queryset = Product.objects.all()

        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        color = self.request.query_params.get('color')
        rating = self.request.query_params.get('rating')
        memory = self.request.query_params.get('memory')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if color:
            queryset = queryset.filter(color__iexact=color)
        if rating:
            queryset = queryset.filter(rating__gte=rating)
        if memory:
            queryset = queryset.filter(memory__iexact=memory)

        return queryset


from rest_framework import viewsets
from .models import Power
from .serializers import PowerSerializer

class PowerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Power.objects.all()
    serializer_class = PowerSerializer


from rest_framework import viewsets
from .models import ProductType
from .serializers import ProductTypeSerializer

class ProductTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    sort_by = request.GET.get('sort_by', 'price')

    if sort_by == 'price':
        products = Product.objects.all().order_by('price')
    elif sort_by == 'rating':
        products = Product.objects.all().order_by('-rating')
    elif sort_by == 'new':
        products = Product.objects.all().order_by('-created_at')
    elif sort_by == 'popularity':
        products = Product.objects.all().order_by('-popularity')
    else:
        products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# shop_category/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Max, Min

from .models import Brand
from .serializers import BrandSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request, *args, **kwargs):
        sort = request.query_params.get('sort')
        qs = self.get_queryset()

        if sort == 'price_asc':
            # Предположим, что у модели Brand есть поле price (число)
            max_price = qs.aggregate(max_price=Max('price'))['max_price']
            if max_price is not None:
                qs = qs.filter(price=max_price)
            else:
                qs = qs.none()

        elif sort == 'price_desc':
            min_price = qs.aggregate(min_price=Min('price'))['min_price']
            if min_price is not None:
                qs = qs.filter(price=min_price)
            else:
                qs = qs.none()

        elif sort == 'rating_desc':
            qs = qs.order_by('-rating')

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SolarPanel
from .serializers import SolarPanelSerializer

class SolarPanelListView(APIView):
    def get(self, request):
        power = request.GET.get('power')  # из query параметра ?power=500
        if power:
            panels = SolarPanel.objects.filter(power=int(power))
        else:
            panels = SolarPanel.objects.all()
        serializer = SolarPanelSerializer(panels, many=True)
        return Response(serializer.data)

