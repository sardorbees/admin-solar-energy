from django.urls import path
from .views import ClickTrackView

urlpatterns = [
    path('api/track-click/', ClickTrackView.as_view(), name='track-click'),
]
