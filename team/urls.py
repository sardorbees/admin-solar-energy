# team/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamMemberViewSet

router = DefaultRouter()
router.register('', TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
