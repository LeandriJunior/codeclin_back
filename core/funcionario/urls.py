from django.urls import re_path
import core.funcionario.views as views
urlpatterns = [
    re_path('pesquisar', views.PesquisarView().as_view())
]