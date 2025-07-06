from django.shortcuts import render, get_object_or_404
from .models import Language
from rest_framework import generics
from rest_framework.exceptions import NotFound
from language.models import Language
from language.serializer import LanguageContentSerializer

def language_list(request):
    languages = Language.objects.all()
    return render(request, 'languages/language_list.html', {'languages': languages})

def language_detail(request, pk):
    language = get_object_or_404(Language, pk=pk)
    return render(request, 'languages/language_detail.html', {'language': language})


def redirect(param):
    pass


def language_add(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('language_list')
    else:
        form = LanguageForm()
    return render(request, 'languages/language_form.html', {'form': form})


class LanguageContentListAPIView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageContentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise NotFound(detail="MainPageContent object not found")
        return obj