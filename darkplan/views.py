# core/views.py
from rest_framework import generics, permissions
from .models import UserTheme
from .serializers import UserThemeSerializer

class UserThemeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserThemeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return UserTheme.objects.get(user=self.request.user)
