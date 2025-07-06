from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]