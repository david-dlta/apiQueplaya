from rest_framework import serializers
from .models import Playa

# Create your models here.

class PlayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playa
        fields = '__all__'
