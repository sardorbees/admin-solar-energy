from rest_framework import generics
from rest_framework.exceptions import NotFound
from category_servicess.admin import CategoryTitle
from category_servicess.serializers import CategoryTitleContentSerializer


class CategoryTitleContentListAPIView(generics.ListAPIView):
    queryset = CategoryTitle.objects.all()
    serializer_class = CategoryTitleContentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise NotFound(detail="CategoryTitle object not found")
        return obj
