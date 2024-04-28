from BO.base.decorators import Response
from model.base.sql import SQLConexao


class AgendaModel(SQLConexao):
    def __init__(self):
        super().__init__()

    @Response(desc_error='Model: Erro ao buscar dados da agenda', is_manter_retorno=True)
    def buscar_agenda(self, condicao=None, is_primeiro=None, parametros=None):
        return self.select(query=f"""
                        SELECT ca.id,
                               ca.titulo AS title,
                               ca.observacao,
                               ca.procedimento,
                               ca.funcionario_id,
                               ca.cliente_id,
                               ca.status,
                               ca.is_concluido,
                               f.nm_completo AS funcionario_agendamento,
                               TO_CHAR(ca.data_ini, 'YYYY-MM-DD"T"HH24:MI:SS') AS start,
                               TO_CHAR(ca.data_fim, 'YYYY-MM-DD"T"HH24:MI:SS') AS end,
                               cac.cor AS color,
                               cac.id AS categoria_id,
                               cac.nome AS categoria_nome
                        FROM {self.schema_cliente}.clinica_agenda AS ca
                        LEFT JOIN {self.schema_cliente}.funcionario f ON f.matricula = ca.funcionario_agendamento_id 
                        LEFT JOIN {self.schema_cliente}.clinica_agenda_categoria cac on cac.id = ca.categoria_id
                        WHERE {condicao}""",
                           parametros=parametros,
                           is_primeiro=is_primeiro)

    @Response(desc_error='Model: Erro ao buscar categorias', is_manter_retorno=True)
    def buscar_categorias(self):
        return self.select(query=f"""
            SELECT id, nome
            FROM {self.schema_cliente}.clinica_agenda_categoria
            WHERE status
            ORDER BY nome
        """)

    @Response(desc_error='Model: Erro ao salvar evento', is_manter_retorno=True)
    def salvar_evento(self, dict_evento=None, is_edicao=False):
        if is_edicao:
            self.update(nm_tabela='clinica_agenda', dict_coluna_valor=dict_evento, filtro_where={'id': dict_evento['id']})
            return
        self.insert(nm_tabela='clinica_agenda', dict_coluna_valor=dict_evento, is_primeiro=False)

    @Response(desc_error='Model: Erro ao habilitar/desabilitar evento', is_manter_retorno=True)
    def trocar_status(self, evento_id=None, status=None):
        self.update(nm_tabela='clinica_agenda', dict_coluna_valor={'status': status}, filtro_where={'id': evento_id})
