from django.urls import re_path
from clinica.agenda import views
urlpatterns = [
    re_path('home', views.HomeView.as_view(), name='home'),
    re_path('evento', views.EventoView.as_view(), name='evento'),
    re_path('evento/status', views.EventoStatusView.as_view(), name='home.status'),
]
