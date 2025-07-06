from django.urls import path
from . import views
from language.views import LanguageContentListAPIView

urlpatterns = [
    path('language-page-content/', LanguageContentListAPIView.as_view(), name='language-page-content'),
    path('', views.language_list, name='language_list'),
    path('language/<int:pk>/', views.language_detail, name='language_detail'),
    path('add/', views.language_add, name='language_add'),
]