from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class TesteView(APIView):
    def get(self, request):
        return JsonResponse({'message': 'Hello World'}, status=200)