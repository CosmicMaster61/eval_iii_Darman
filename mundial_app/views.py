from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from mundial_api.serializers import EquipoSerializer, JugadorSerializer
from mundial_api.models import Jugador, Equipo

def mostrarEquipos(request):
    equipo = Equipo.objects.all()
    data = {'equipo': equipo}
    return render(request, 'lista_equipos.html', data)

def mostrarEquipo(request, id):
    equipo = Equipo.objects.filter(id=id).first()
    data = {'equipo': equipo}
    return render(request, 'muestra_equipo.html', data)


