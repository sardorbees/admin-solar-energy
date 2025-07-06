from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YourModelViewSet
from django.contrib import admin
router = DefaultRouter()
router.register(r'yourmodel', YourModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]