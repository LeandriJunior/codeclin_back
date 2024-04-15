from django.db import models

import core.models


# Create your models here.

class Agenda(core.models.Log):
    titulo = models.CharField(max_length=256, null=True)
    observacao = models.CharField(max_length=512, null=True)
    procedimento = models.CharField(max_length=512, null=True)
    data_ini = models.DateTimeField(null=True)
    data_fim = models.DateTimeField(null=True)
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.DO_NOTHING, null=True)
    funcionario = models.ForeignKey('funcionario.Funcionario', on_delete=models.DO_NOTHING, null=True, related_name='agenda_funcionario')
    funcionario_agendamento = models.ForeignKey('funcionario.Funcionario', on_delete=models.DO_NOTHING, null=True, related_name='funcionario_agendamento')
    categoria = models.ForeignKey('CategoriaAgenda', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = u'clinica_agenda'


class CategoriaAgenda(core.models.Log):
    nome = models.CharField(max_length=256, null=True)
    descricao = models.CharField(max_length=512, null=True)
    cor = models.CharField(max_length=7, null=True)

    class Meta:
        db_table = u'clinica_agenda_categoria'
