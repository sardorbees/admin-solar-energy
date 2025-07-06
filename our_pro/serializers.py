from rest_framework import serializers
from .models import Work, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        ref_name = 'Textkjnkcj'

class WorkSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Work
        fields = '__all__'
        ref_name = 'WorkTxt'
