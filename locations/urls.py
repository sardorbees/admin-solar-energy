from rest_framework.routers import DefaultRouter
from .views import LocationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
