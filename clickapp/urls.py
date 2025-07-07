# security/urls.py
from django.urls import path
from .views import register_click

urlpatterns = [
    path('api/click/', register_click, name='register_click'),
]
