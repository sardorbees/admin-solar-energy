from django.urls import path

from category_servicess.views import CategoryTitleContentListAPIView

urlpatterns = [
    path('category-title-content/', CategoryTitleContentListAPIView.as_view(), name='category-title-content')
]