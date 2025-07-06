from django.urls import path
from .views import WorkListCreateAPIView, WorkDetailAPIView

urlpatterns = [
    path('works/', WorkListCreateAPIView.as_view(), name='work-list'),
    path('works/<int:pk>/', WorkDetailAPIView.as_view(), name='work-detail'),
]
