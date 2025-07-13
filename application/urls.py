from django.urls import path
from .views import ApplicationCreateView, UnlockIPView

urlpatterns = [
    path('applicationapplications/', ApplicationCreateView.as_view(), name='application-create'),
    path('unlock-ip/', UnlockIPView.as_view(), name='unlock-ip'),
]
