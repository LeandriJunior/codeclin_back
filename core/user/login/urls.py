from django.urls import re_path
import core.user.login.views as views
urlpatterns = [
    re_path('login', views.LoginUserView.as_view(), name='login'),
    re_path('register', views.RegisterUserView.as_view(), name='registrar')
]