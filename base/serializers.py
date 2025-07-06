from rest_framework import serializers

from base.models import *


class MainPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageContent
        fields = "__all__"
        read_only_fields = [fields]


class MainPageCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageCard
        fields = "__all__"
        read_only_fields = [fields]


class MainPageServiceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageServiceCard
        fields = "__all__"
        read_only_fields = [fields]


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = "__all__"
        read_only_fields = [fields]


