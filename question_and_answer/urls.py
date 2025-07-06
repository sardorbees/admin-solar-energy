from django.urls import path, include
from . import views
from django.contrib import admin

from question_and_answer.views import AnswerContentListAPIView
from question_and_answer.views import QuestionManagerListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.question_list, name='question_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('answer-manager-content/', AnswerContentListAPIView.as_view(), name='answer-manager-content'),
    path('question-manager-content/', QuestionManagerListAPIView.as_view(), name='question-manager-content'),
]
