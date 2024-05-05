from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from BO.user.funcionario import Funcionario as Funcionario


class PesquisarView(APIView):
    def get(self, request):
        response = Funcionario().buscar_funcionarios_pesquisa(
            pesquisa=self.request.GET.get('pesquisa')
        )
        return JsonResponse(response, safe=False, status=200)
