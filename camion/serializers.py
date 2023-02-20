from rest_framework import serializers
from .models import Camion, Conductor, Gastos

class CamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camion
        fields = "__all__"

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = "__all__"

class GastosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gastos
        fields = "__all__"


