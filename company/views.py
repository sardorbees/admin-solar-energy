from django.shortcuts import render, get_object_or_404
from .models import Company
from rest_framework import generics
from rest_framework.exceptions import NotFound
from company.admin import Company
from company.serializers import CompanyContentSerializer

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company/company_list.html', {'companies': companies})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company/company_detail.html', {'company': company})


class CompanyContentListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyContentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise NotFound(detail="CategoryTitleText object not found")
        return obj
