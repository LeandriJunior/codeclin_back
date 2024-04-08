from django.urls import re_path, include

import core.views as views
import core.user.urls
urlpatterns = [
    re_path('teste', views.TesteView().as_view(), name='teste_view'),
    re_path('user', include(core.user.urls))
]
