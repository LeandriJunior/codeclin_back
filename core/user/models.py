import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, Permission, Group, UserManager
from django.utils.translation import gettext_lazy as _

import core.models


class Profile(AbstractBaseUser, core.models.Log, PermissionsMixin):
    tipo_conta = models.CharField(null=True, max_length=200, default='usr')
    username = models.CharField(max_length=200, unique=True)
    USERNAME_FIELD = 'username'
    is_staff = models.BooleanField(null=True, default=False)
    is_atualizar_sessao = models.BooleanField(default=False, null=True)
    is_primeiro_login = models.BooleanField(default=True, null=True)
    is_resetar_senha = models.BooleanField(default=False, null=True)
    senha_padrao = models.CharField(null=True, max_length=200)
    email = models.EmailField(max_length=200, null=True)
    objects = BaseUserManager()
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )

    class Meta:
        abstract = True


class UserLogin(Profile):
    usuario = models.OneToOneField('User', on_delete=models.DO_NOTHING, null=True)
    nm_primeiro = models.CharField(max_length=200, null=True)
    nm_ultimo = models.CharField(max_length=200, null=True)
    objects = UserManager()

    class Meta:
        db_table = 'user_login'


class User(core.models.Log, core.models.PessoaLog):
    endereco = models.ForeignKey('core.Endereco', on_delete=models.DO_NOTHING, null=True, related_name='endereco')
    is_cliente = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'


class Cargo(core.models.Log):
    nome = models.CharField(max_length=200, primary_key=True)
    cargo_pai = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)
    nm_descritivo = models.CharField(max_length=500, null=True)
    template_descricao = models.TextField(null=True)
    funcao = models.CharField(max_length=200, null=True)
    is_farma = models.BooleanField(default=False)
    cd_externo = models.IntegerField(null=True)
    is_loja = models.BooleanField(default=False)

    class Meta:
        db_table = "user_cargo"


class Grupo(core.models.Log):
    nivel = models.IntegerField(null=True)
    nome = models.CharField(max_length=200, primary_key=True)
    nm_descritivo = models.CharField(max_length=200, null=True)
    descricao = models.CharField(max_length=500, null=True)
    grupo_pai = models.ForeignKey('user.Grupo', on_delete=models.DO_NOTHING, null=True,
                                  related_name='%(app_label)s_%(class)s_grupo_pai')
    tela_principal_referencia = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "user_grupo"


class GrupoUser(core.models.Log):
    grupo = models.ForeignKey('user.Grupo', on_delete=models.DO_NOTHING, null=True)
    usuario = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, null=True)
    codigo = models.IntegerField(null=True, help_text='Código da área que o grupo faz parte')
    cd_tipo_area = models.CharField(null=True, max_length=200, help_text='Código do tipo da área que o grupo faz parte')
    tipo = models.CharField(max_length=200, null=True)
    tela_principal = models.CharField(max_length=128, null=True)
    ordem = models.IntegerField(null=True)

    class Meta:
        db_table = "user_grupo_user"


class Perfil(core.models.Log):
    nome = models.CharField(max_length=256, null=True)
    descricao = models.CharField(max_length=512, null=True)
    modulo = models.CharField(max_length=128, null=True)
    perfil_pai = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "user_perfil"


class PerfilPontoFuncao(core.models.Log):
    ponto_funcao = models.ForeignKey('core.PontoFuncao', on_delete=models.DO_NOTHING, null=True)
    perfil = models.ForeignKey('Perfil', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "user_perfil_pontofuncao"


class PerfilUser(core.models.Log):
    usuario = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, null=True)
    perfil = models.ForeignKey('Perfil', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "user_perfil_user"