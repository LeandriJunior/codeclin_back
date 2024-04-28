from datetime import datetime

import model.clinica.agenda
from BO.base.decorators import Response
import model.clinica.agenda as agendaModel
import BO.user.funcionario as funcionario
import BO.user.cliente as cliente
import model.user.funcionario

class Agenda:
    def __init__(self, evento_id=None):
        self.evento_id = evento_id

    @Response(desc_error='Erro ao buscar dados da agenda', lista_retornos=['agenda'])
    def buscar_agenda(self, data_ini=None, data_fim=None, agenda_id=None, is_ativo=True, is_primeiro=False):
        condicao = '1=1'
        if data_ini:
            data_ini = datetime.strptime(data_ini, "%d/%m/%Y %H:%M:%S")
            condicao += ' AND ca.data_ini > :data_ini'
        if data_fim:
            data_fim = datetime.strptime(data_fim, "%d/%m/%Y %H:%M:%S")
            condicao += ' AND ca.data_fim < :data_fim'

        if agenda_id:
            condicao += ' AND ca.id = :agenda_id'

        if is_ativo:
            condicao += ' AND ca.status'

        parametros = {'data_ini': data_ini, 'data_fim': data_fim, 'agenda_id': agenda_id}

        return agendaModel.AgendaModel().buscar_agenda(condicao=condicao, is_primeiro=is_primeiro, parametros=parametros)

    @Response(desc_error='Erro ao buscar o evento', lista_retornos=['evento'])
    def buscar_evento(self):
        agenda = []
        if self.evento_id:
            agenda = self.buscar_agenda(
                agenda_id=self.evento_id,
                is_primeiro=True,
                is_ativo=True
            )['agenda']

        return {
            'agenda': agenda,
            'lista_funcionarios': funcionario.Funcionario().buscar_funcionarios()['lista_funcionarios'],
            'lista_clientes': cliente.Cliente().buscar_clientes()['lista_clientes'],
        }

    @Response(desc_error='Erro ao salvar evento')
    def salvar_evento(self, cliente_id=None, funcionario_id=None, funcionario_funcionamento_id=None, data_ini=None, data_fim=None, procedimento=None,
                      observacao=None):
        is_edicao=False
        if data_ini:
            data_ini = datetime.strptime(data_ini, '%d/%m/%Y %H:%M:%S')
        if data_fim:
            data_fim = datetime.strptime(data_fim, '%d/%m/%Y %H:%M:%S')

        dict_evento = {
            'titulo': model.user.funcionario.FuncionarioModel().buscar_funcionarios_combo(funcionario_id=funcionario_id, is_primeiro=True)['nm_completo'],
            'observacao': observacao,
            'funcionario_id': funcionario_id,
            'cliente_id': cliente_id,
            'procedimento': procedimento,
            'data_ini': data_ini,
            'data_fim': data_fim,
            'status': True,
            'dat_insercao': datetime.now()
        }

        if self.evento_id:
            is_edicao=True
            dict_evento['id'] = self.evento_id
            dict_evento.pop('dat_insercao')
            dict_evento['dat_edicao'] = datetime.now()

        model.clinica.agenda.AgendaModel().salvar_evento(dict_evento, is_edicao=is_edicao)

    @Response(desc_error='Erro ao buscar categorias ', lista_retornos=['lista_categorias'])
    def buscar_categorias(self):
        return model.clinica.agenda.AgendaModel().buscar_categorias()

    @Response(desc_error='Erro ao habilitar/desabilitar evento', lista_retornos=['novo_status'])
    def trocar_status(self, status=True):
        return model.clinica.agenda.AgendaModel().trocar_status(
            evento_id=self.evento_id,
            status=status
        )


