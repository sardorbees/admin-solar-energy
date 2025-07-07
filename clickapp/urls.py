from django.urls import path
from .views import ClickMonitorAPIView

urlpatterns = [
    path('api/monitor-clicks/', ClickMonitorAPIView.as_view(), name='monitor-clicks'),
]
