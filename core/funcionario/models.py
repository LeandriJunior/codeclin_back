from django.db import models
import core.models


class Funcionario(core.models.Log, core.models.PessoaLog):
    user = models.OneToOneField('user.User', on_delete=models.DO_NOTHING, null=True)
    dat_admissao = models.DateTimeField(null=True)
    matricula = models.CharField(max_length=200, primary_key=True)
    cargo = models.ForeignKey('Cargo', on_delete=models.DO_NOTHING, null=True)
    is_adm = models.BooleanField(null=True, default=False)
    funcionario_responsavel = models.ForeignKey(
        'self', on_delete=models.DO_NOTHING, null=True,  related_name='%(app_label)s_%(class)s_funcionarioresponsavel',
    )
    email = models.EmailField(max_length=200, null=True)

    numero_cadastro_regional = models.CharField(max_length=200, null=True)
    tipo_cadastro_regional = models.CharField(max_length=200, null=True)

    endereco = models.ForeignKey('core.Endereco', on_delete=models.DO_NOTHING, null=True,  related_name='%(app_label)s_%(class)s_endereco')

    class Meta:
        db_table = u'funcionario'


class Cargo(core.models.Log):
    nome = models.CharField(max_length=200, primary_key=True)
    cargo_pai = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, related_name='%(app_label)s_%(class)s_cargopai')
    nm_descritivo = models.CharField(max_length=500, null=True)
    is_cadastro_regional = models.BooleanField(default=False)

    class Meta:
        db_table = u'funcionario_cargo'


class Grupo(core.models.Log):
    nivel = models.IntegerField(null=True)
    nome = models.CharField(max_length=200, primary_key=True)
    nm_descritivo = models.CharField(max_length=200, null=True)
    descricao = models.CharField(max_length=500, null=True)
    grupo_pai = models.ForeignKey('Grupo', on_delete=models.DO_NOTHING, null=True,
                                  related_name='%(app_label)s_%(class)s_grupo_pai')
    tela_principal_referencia = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "funcionario_grupo"


class GrupoUser(core.models.Log):
    grupo = models.ForeignKey('Grupo', on_delete=models.DO_NOTHING, null=True)
    funcionario = models.ForeignKey('Funcionario', on_delete=models.DO_NOTHING, null=True)
    codigo = models.IntegerField(null=True, help_text='Código da área que o grupo faz parte')
    cd_tipo_area = models.CharField(null=True, max_length=200, help_text='Código do tipo da área que o grupo faz parte')
    tipo = models.CharField(max_length=200, null=True)
    tela_principal = models.CharField(max_length=128, null=True)
    ordem = models.IntegerField(null=True)

    class Meta:
        db_table = "funcionario_grupofuncionario"


class Perfil(core.models.Log):
    nome = models.CharField(max_length=256, null=True)
    descricao = models.CharField(max_length=512, null=True)
    modulo = models.CharField(max_length=128, null=True)
    perfil_pai = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "funcionario_perfil"


class PerfilPontoFuncao(core.models.Log):
    ponto_funcao = models.ForeignKey('core.PontoFuncao', on_delete=models.DO_NOTHING, null=True)
    perfil = models.ForeignKey('Perfil', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "funcionario_perfilpontofuncao"


class PerfilUser(core.models.Log):
    funcionario = models.ForeignKey('Funcionario', on_delete=models.DO_NOTHING, null=True)
    perfil = models.ForeignKey('Perfil', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "funcionario_perfilfuncionario"



class PontoFuncaoFuncionario(core.models.Log):
    ponto_funcao = models.ForeignKey('core.PontoFuncao', on_delete=models.DO_NOTHING, null=True)
    funcionario = models.ForeignKey('Funcionario', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "funcionario_pontofuncaofuncionario"