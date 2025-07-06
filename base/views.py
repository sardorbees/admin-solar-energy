from rest_framework import generics
from rest_framework.exceptions import NotFound

from base.models import *
from base.serializers import *


class MainPageContentListAPIView(generics.RetrieveAPIView):
    queryset = MainPageContent.objects.all()
    serializer_class = MainPageContentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise NotFound(detail="MainPageContent object not found")
        return obj


class MainPageCardListAPIView(generics.ListAPIView):
    queryset = MainPageCard.objects.all()
    serializer_class = MainPageCardSerializer


class MainPageServiceCardListAPIView(generics.ListAPIView):
    queryset = MainPageServiceCard.objects.all()
    serializer_class = MainPageServiceCardSerializer


class BannerImageListAPIView(generics.ListAPIView):
    queryset = BannerImage.objects.filter(is_published=True)
    serializer_class = BannerImageSerializer
