from django.db import models
import core.models


class Filial(core.models.Log):
    codigo = models.IntegerField(null=True)
    nome = models.CharField(max_length=200, null=True)
    tipo = models.CharField(max_length=200, null=True)
    cnpj = models.CharField(max_length=200, null=True)
    inscricao_estadual = models.CharField(max_length=200, null=True)
    cnes = models.CharField(max_length=200, null=True)
    razao_social = models.CharField(max_length=200, null=True)
    nome_fantasia = models.CharField(max_length=200, null=True)
    data_abertura = models.DateField(null=True)
    data_fechamento = models.DateField(null=True)
    telefone = models.CharField(max_length=200, null=True)
    celular = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    endereco = models.ForeignKey('core.Endereco', on_delete=models.DO_NOTHING, null=True,  related_name='%(app_label)s_%(class)s_endereco')
    area = models.ForeignKey('filial.Area', on_delete=models.DO_NOTHING, null=True, related_name='%(app_label)s_%(class)s_area')
    responsavel = models.ForeignKey('funcionario.Funcionario', on_delete=models.DO_NOTHING, null=True, related_name='%(app_label)s_%(class)s_funcionarioresponsavel')

    class Meta:
        db_table = 'filial'


class Area(core.models.Log):
    nome = models.CharField(max_length=200, null=True)
    area_pai = models.ForeignKey('filial.Area', on_delete=models.DO_NOTHING, null=True, related_name='%(app_label)s_%(class)s_area')
    responsavel = models.ForeignKey('funcionario.Funcionario', on_delete=models.DO_NOTHING, null=True,  related_name='%(app_label)s_%(class)s_funcionarioresponsavel')
    tipo = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'filial_area'

