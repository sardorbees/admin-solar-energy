# products/urls.py
from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('search/', ProductListView.as_view(), name='product-search'),
]
