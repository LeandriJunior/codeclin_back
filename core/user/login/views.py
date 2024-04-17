from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from rest_framework.views import APIView
import BO.user.login as loginBO
import core.user.models


class LoginUserView(APIView):
    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        sistema = loginBO.Login(
                                request=self.request,
                                username=username,
                                password=password
                                )

        response = sistema.login(request=request)

        return JsonResponse(response, status=response['status_code'])


class RegisterUserView(APIView):
    # Classe temporaria, apenas para registrar pessoas momentaniamente
    def post(self, request):
        try:
            response = json.loads(self.request.body)
            username = f"{response['nm_primeiro']}.{response['nm_ultimo']}"
            core.user.models.UserLogin.objects.create_user(username=username,
                                                      email=response['email'],
                                                      password=response['password'],
                                                      nm_primeiro=response['nm_primeiro'],
                                                      nm_ultimo=response['nm_ultimo'])

            status = {'status': True}
        except Exception as e:
            status = {'status': False,
                      'description': e}
        return JsonResponse(status, flat=True, status=200)