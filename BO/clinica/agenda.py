from datetime import datetime

from BO.base.decorators import Response
import model.clinica.agenda as agendaModel
import BO.user.funcionario as funcionario
import BO.user.cliente as cliente
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
        agenda = self.buscar_agenda(
            agenda_id=self.evento_id,
            is_primeiro=True,
            is_ativo=True
        )['agenda']

        return {
            'agenda': agenda,
            'lista_funcionarios': funcionario.Funcionario().buscar_funcionarios()['lista_funcionarios'],
            'lista_clientes': cliente.Cliente().buscar_clientes()['lista_clientes']
        }

    @Response(desc_error='Erro ao salvar evento', lista_retornos=['evento'])
    def salvar_evento(self, cliente_id=None, funcionario_id=None, funcionario_funcionamento_id=None, data_ini=None, data_fim=None, procedimento=None,
                      observacao=None):
        return True


