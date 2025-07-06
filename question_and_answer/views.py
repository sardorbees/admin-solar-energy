from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from rest_framework import generics
from rest_framework.exceptions import NotFound

from question_and_answer.models import Answer
from question_and_answer.serializers import AnswerPageContentSerializer

from question_and_answer.models import Question
from question_and_answer.serializers import QuestionManagerSerializer

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_and_answer/question_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_and_answer/question_detail.html', {'question': question})



class AnswerContentListAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerPageContentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise NotFound(detail="BannerImage object not found")
        return obj


class QuestionManagerListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionManagerSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise NotFound(detail="BannerImage object not found")
        return obj