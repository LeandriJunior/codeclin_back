from django.urls import re_path, include
import clinica.agenda.urls
urlpatterns = [
    re_path('agenda', include(clinica.agenda.urls))
]