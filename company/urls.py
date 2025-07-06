from django.urls import path
from . import views
from django.contrib import admin

from company.views import CompanyContentListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.company_list, name='company_list'),
    path('<int:pk>/', views.company_detail, name='company_detail'),
    path('company-content-list/', CompanyContentListAPIView.as_view(), name='company-content-list')
]
