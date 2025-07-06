from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TariffPlanViewSet

router = DefaultRouter()
router.register(r'tariffs', TariffPlanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
