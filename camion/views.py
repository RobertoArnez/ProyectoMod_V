from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Camion, Viaje, Conductor, Gastos
from .serializers import CamionSerializer, ConductorSerializer, GastosSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

def index(request):
    return HttpResponse("Esta es la aplicacion de administracion de camiones")


class CamionViewSet(viewsets.ModelViewSet):
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

class GastosViewSet(viewsets.ModelViewSet):
    queryset = Gastos.objects.all()
    serializer_class = GastosSerializer

@api_view(["GET"])
def viajes_count(request):
    try:
        cantidad = Viaje.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)

