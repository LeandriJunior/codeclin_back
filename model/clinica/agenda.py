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
                               ca.descricao,
                               TO_CHAR(ca.data_ini, 'YYYY-MM-DD"T"HH24:MI:SS') AS start,
                               TO_CHAR(ca.data_fim, 'YYYY-MM-DD"T"HH24:MI:SS') AS end,
                               cac.cor AS color,
                               cac.id AS categoria_id,
                               cac.nome AS categoria_nome
                        FROM {self.schema_cliente}.clinica_agenda AS ca
                        LEFT JOIN {self.schema_cliente}.clinica_agenda_categoria cac on cac.id = ca.categoria_id
                        WHERE {condicao}""",
                           parametros=parametros,
                           is_primeiro=is_primeiro)
