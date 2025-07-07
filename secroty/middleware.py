from django.shortcuts import HttpResponse
from clickapp.models import BlockedIP

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponse("Вы заблокированы из-за подозрительной активности", status=403)
        return self.get_response(request)
