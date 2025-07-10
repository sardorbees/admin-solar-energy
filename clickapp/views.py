import requests
from django.utils.timezone import now
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import VisitorClick

class TrackClickView(APIView):
    def post(self, request):
        ip = self.get_client_ip(request)
        user_agent = request.headers.get('User-Agent', '')
        click_threshold = 1000  # max 10 clicks per 5 sec

        obj, created = VisitorClick.objects.get_or_create(ip=ip, user_agent=user_agent)

        # Если уже вручную заблокирован — не продолжаем
        if obj.blocked:
            return JsonResponse({"blocked": True})

        # Автоклик логика
        time_diff = now() - obj.last_click
        if time_diff.total_seconds() < 5:
            obj.clicks += 1
        else:
            obj.clicks = 1

        # Автоалерт, но блокируем только вручную!
        if obj.clicks >= click_threshold:
            self.send_telegram_alert(ip, user_agent, obj.clicks)

        obj.save()

        return JsonResponse({"blocked": obj.blocked})

    def get_client_ip(self, request):
        return request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))

    def send_telegram_alert(self, ip, agent, count):
        token = '7307767852:AAG7yPzsRWCmZHkq5phcE-x8yySkW99ecxo'
        chat_id = '7139975148'
        msg = f'⚠️ Обнаружен автоклик:\nIP: {ip}\nAgent: {agent}\nClicks: {count}\n❗ Заблокируйте вручную в админке.'
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={
            'chat_id': chat_id,
            'text': msg
        })