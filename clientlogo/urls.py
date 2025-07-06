from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientLogoViewSet

router = DefaultRouter()
router.register(r'clients', ClientLogoViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]
