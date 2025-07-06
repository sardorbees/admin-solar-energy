from rest_framework import generics
from rest_framework.exceptions import NotFound
from category_title_text.admin import Category_Title_Text
from category_title_text.serializer import CategoryTitleTextContentSerializer


class CategoryTitleTextContentListAPIView(generics.ListAPIView):
    queryset = Category_Title_Text.objects.all()
    serializer_class = CategoryTitleTextContentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise NotFound(detail="CategoryTitleText object not found")
        return obj
