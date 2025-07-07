from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta

from .models import IPClick, BlockedIP

class ClickTrackView(APIView):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')

    def post(self, request):
        ip = self.get_client_ip(request)

        if BlockedIP.objects.filter(ip=ip).exists():
            return Response({'blocked': True}, status=status.HTTP_403_FORBIDDEN)

        # логируем клик
        IPClick.objects.create(ip=ip)

        # считаем количество кликов за последние 60 секунд
        time_threshold = timezone.now() - timedelta(seconds=60)
        recent_clicks = IPClick.objects.filter(ip=ip, timestamp__gte=time_threshold).count()

        if recent_clicks > 30:
            BlockedIP.objects.get_or_create(ip=ip)
            return Response({'blocked': True}, status=status.HTTP_403_FORBIDDEN)

        return Response({'blocked': False}, status=status.HTTP_200_OK)
