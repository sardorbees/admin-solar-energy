from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserProfileView, LogoutView, DashboardView
from .serializers import CustomTokenSerializer

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", CustomLoginView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("profile/", UserProfileView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("edit-profile/", UserProfileView.as_view(), name="edit-profile"),
    path("dashboard/", DashboardView.as_view()),
]
