from rest_framework import viewsets
from .models import ClientLogo
from .serializers import ClientLogoSerializer

class ClientLogoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClientLogo.objects.all()
    serializer_class = ClientLogoSerializer
