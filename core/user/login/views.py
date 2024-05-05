from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from rest_framework.views import APIView

import BO.user.login
import BO.user.login as loginBO
import core.user.models


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.response import Response

from BO.user.sessao import Sessao


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user

        # Aqui você pode adicionar lógica personalizada para criar a sessão de usuário
        # Por exemplo, salvar informações adicionais sobre a sessão no banco de dados,
        # registrar o horário de login, etc.

        return JsonResponse({
            'access': str(AccessToken.for_user(user)),
            'refresh': str(RefreshToken.for_user(user)),
            'sessao': Sessao(user_id=user.pk).get_sessao()
        })




class RegisterUserView(APIView):
    # Classe temporaria, apenas para registrar pessoas momentaniamente
    def post(self, request):
        try:
            response = json.loads(self.request.body)
            username = f"{response['nm_primeiro']}.{response['nm_ultimo']}"
            core.user.models.User.objects.create_user(username=username,
                                                      email=response['email'],
                                                      password=response['password'],
                                                      nm_primeiro=response['nm_primeiro'],
                                                      nm_ultimo=response['nm_ultimo'])

            status = {'status': True}
        except Exception as e:
            status = {'status': False,
                      'description': e}
        return JsonResponse(status, flat=True, status=200)