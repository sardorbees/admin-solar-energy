from rest_framework import generics
from rest_framework.exceptions import NotFound
from category_title.admin import CategoryTitle
from category_title.serializer import CategoryTitleContentSerializer


class CategoryTitleContentListAPIView(generics.ListAPIView):
    queryset = CategoryTitle.objects.all()
    serializer_class = CategoryTitleContentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise NotFound(detail="CategoryTitle object not found")
        return obj
