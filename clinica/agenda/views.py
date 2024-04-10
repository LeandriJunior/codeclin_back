from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

import BO.clinica.agenda


# Create your views here.
class HomeView(APIView):
    def get(self, request):
        response = BO.clinica.agenda.Agenda().buscar_agenda(
            data_ini=self.request.GET.get('data_ini'),
            data_fim=self.request.GET.get('data_fim')
        )
        return JsonResponse(response, safe=False, status=response['status_code'])


class EventoView(APIView):
    def get(self, request):
        response = BO.clinica.agenda.Agenda(evento_id=self.request.GET.get('evento_id')).buscar_evento()
        return JsonResponse(response, safe=False, status=response['status_code'])
