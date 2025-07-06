from django.urls import path
from .views import CardListAPIView

urlpatterns = [
    path('api/cards/', CardListAPIView.as_view(), name='card-list'),
]
