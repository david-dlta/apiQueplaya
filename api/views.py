from django.shortcuts import render
from rest_framework import viewsets

from .models import Playa
from .serializers import PlayaSerializer

# Create your views here.
class PlayaViewSet(viewsets.ModelViewSet):
    serializer_class = PlayaSerializer
    queryset = Playa.objects.all()

class TopPlayaViewSet(viewsets.ModelViewSet):
    serializer_class = PlayaSerializer
    queryset = Playa.objects.raw(
        'SELECT * FROM db1.api_playa ORDER BY ID ASC limit 1'
    )