# views.py
from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.response import Response
from rest_framework import status
import requests

TELEGRAM_TOKEN = '7614226832:AAGUGKTBy0J5HpBj9Pyuh4uUIco2GTmWADE'
TELEGRAM_CHAT_ID = '7139975148'

class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        application = serializer.save()
        self.send_telegram_notification(application)

    def send_telegram_notification(self, application):
        message = (
            f"📥 Новая заявка на дезинфекцию\n"
            f"👤 Имя: {application.full_name}\n"
            f"📞 Телефон: {application.phone}\n"
            f"🏠 Адрес: {application.address}\n"
            f"📝 Описание: {application.description}"
        )
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})