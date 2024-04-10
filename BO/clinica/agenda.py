from datetime import datetime

from BO.base.decorators import Response
from model.base.sql import SQLConexao


class Agenda(SQLConexao):
    def __init__(self):
        super().__init__()

    @Response(desc_error='Erro ao buscar dados da agenda', lista_retornos=['agenda'])
    def buscar_agenda(self, data_ini=None, data_fim=None):
        condicao = 'ca.status'
        if data_ini:
            data_ini = datetime.strptime(data_ini, "%d/%m/%Y %H:%M:%S")
            condicao += ' AND ca.data_ini > :data_ini'
        if data_fim:
            data_fim = datetime.strptime(data_fim, "%d/%m/%Y %H:%M:%S")
            condicao += ' AND ca.data_fim < :data_fim'
        return self.select(query=f"""
                SELECT ca.id,
                       ca.titulo AS title,
                       ca.descricao,
                       TO_CHAR(ca.data_ini, 'YYYY-MM-DD"T"HH24:MI:SS') AS start,
                       TO_CHAR(ca.data_fim, 'YYYY-MM-DD"T"HH24:MI:SS') AS end,
                       cac.cor AS color
                FROM {self.schema_cliente}.clinica_agenda AS ca
                LEFT JOIN {self.schema_cliente}.clinica_agenda_categoria cac on cac.id = ca.categoria_id
                WHERE {condicao}""",
            parametros={'data_ini': data_ini, 'data_fim':data_fim})