# gallery/urls.py
from django.urls import path
from .views import ImageListAPIView

urlpatterns = [
    path('images/', ImageListAPIView.as_view(), name='image-list'),
]
