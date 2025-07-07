from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClickBlock
from .serializers import ClickBlockSerializer
import requests

TELEGRAM_BOT_TOKEN = '7307767852:AAG7yPzsRWCmZHkq5phcE-x8yySkW99ecxo'
TELEGRAM_CHAT_ID = '7139975148'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        requests.post(url, data=data)
    except:
        pass

class ClickMonitorAPIView(APIView):
    def post(self, request):
        ip = request.META.get('REMOTE_ADDR')
        user_agent = request.headers.get('User-Agent')
        click_count = int(request.data.get('clicks', 0))

        obj, created = ClickBlock.objects.get_or_create(ip_address=ip, user_agent=user_agent)

        obj.click_count += click_count
        if obj.click_count > 20:  # Порог кликов
            obj.blocked = True
            send_telegram_message(f"🚨 AutoClick Detected!\nIP: {ip}\nAgent: {user_agent}")
        obj.save()

        return Response({"blocked": obj.blocked}, status=200)
