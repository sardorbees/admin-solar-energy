from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, CategoryViewSet,
    PowerViewSet, ProductTypeViewSet, BrandViewSet, product_list,
    SolarPanelListView
)

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('power', PowerViewSet, basename='power')
router.register('producttype', ProductTypeViewSet, basename='producttype')
router.register('categories', CategoryViewSet)
router.register('brand', BrandViewSet, basename='brand')

extra_urls = [
    path('products/sorted/', product_list, name='product-list'),
    path('solar-panels/', SolarPanelListView.as_view(), name='solar-panel-list'),
]

urlpatterns = router.urls + extra_urls
