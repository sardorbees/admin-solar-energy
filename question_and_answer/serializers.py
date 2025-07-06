from rest_framework import serializers
from question_and_answer.models import Answer
from question_and_answer.models import Question

class AnswerPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        read_only_fields = [fields]


class QuestionManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = [fields]
