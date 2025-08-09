# laptops/urls.py
from django.urls import path
from .views import LaptopListCreateView, LaptopRetrieveUpdateDestroyView

urlpatterns = [
    path('laptops/', LaptopListCreateView.as_view(), name='laptop-list'),
    path('laptops/<slug:slug>/', LaptopRetrieveUpdateDestroyView.as_view(), name='laptop-detail'),
]
