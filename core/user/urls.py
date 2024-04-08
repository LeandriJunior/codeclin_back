from django.urls import re_path, include
import core.user.login.urls
urlpatterns = [
    re_path('', include(core.user.login.urls))
]