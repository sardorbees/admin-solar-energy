from django.urls import path

from category_title_text.views import CategoryTitleTextContentListAPIView

urlpatterns = [
    path('category-title-text/', CategoryTitleTextContentListAPIView.as_view(), name='category-title-text')
]