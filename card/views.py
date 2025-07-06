from rest_framework import generics
from .models import Card
from .serializers import CardSerializer

class CardListAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
