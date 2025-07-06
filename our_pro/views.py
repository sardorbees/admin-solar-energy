from rest_framework import generics
from .models import Work
from .serializers import WorkSerializer

class WorkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Work.objects.all().order_by('-completed_at')
    serializer_class = WorkSerializer

class WorkDetailAPIView(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
