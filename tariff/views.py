from rest_framework import viewsets
from .models import TariffPlan
from .serializers import TariffPlanSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

class TariffPlanViewSet(viewsets.ModelViewSet):
    queryset = TariffPlan.objects.all()
    serializer_class = TariffPlanSerializer

    @action(detail=False, methods=['get'])
    def today_discounts(self, request):
        today = timezone.localdate()
        tariffs = [t for t in TariffPlan.objects.filter(is_active=True) if t.is_today_applicable()]
        serializer = self.get_serializer(tariffs, many=True)
        return Response(serializer.data)
