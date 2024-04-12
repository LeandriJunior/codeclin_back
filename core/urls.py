from django.urls import re_path, include

import core.views as views
import core.user.urls
import core.funcionario.urls
urlpatterns = [
    re_path('teste', views.TesteView().as_view(), name='teste_view'),
    re_path('user', include(core.user.urls)),
    re_path('funcionario', include(core.funcionario.urls))
]
