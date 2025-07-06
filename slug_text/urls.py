from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SlugCategoryViewSet
from django.contrib import admin
router = DefaultRouter()
router.register(r'slug_category', SlugCategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]