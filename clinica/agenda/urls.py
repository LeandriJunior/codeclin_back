from django.urls import re_path
from clinica.agenda import views
urlpatterns = [
    re_path('home', views.HomeView.as_view(), name='home')
]