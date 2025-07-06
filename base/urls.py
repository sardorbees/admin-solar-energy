from django.urls import path

from base.views import *

urlpatterns = [
    path('main-page-content/', MainPageContentListAPIView.as_view(), name='main-page-content'),
    path('main-page-card/', MainPageCardListAPIView.as_view(), name='main-page-card'),
    path('main-page-service-card/', MainPageServiceCardListAPIView.as_view(), name='main-page-service-card'),
    path('banner-image/', BannerImageListAPIView.as_view(), name='banner-image')
]