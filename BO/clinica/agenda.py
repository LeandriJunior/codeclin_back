from BO.base.decorators import Response
from model.base.sql import SQLConexao


class Agenda(SQLConexao):
    def __init__(self):
        super().__init__()

    @Response(desc_error='Erro ao buscar dados da agenda', lista_retornos=['agenda'])
    def buscar_agenda(self):
        return [
            {
                'id': 1,
                'title': 'Fernando Wagner',
                'color': '#fc0701',
                'start': '2024-04-09' + 'T10:00:00',
                'end': '2024-04-09' + 'T10:30:00'
            },
            {
                'id': 2,
                'title': 'Sara Jessica',
                'color': '#009301',
                'start': '2024-04-09' + 'T15:15:00',
                'end': '2024-04-09' + 'T16:00:00'
            },
            {
                'id': 3,
                'title': 'Leandri Albert Wagner Junior',
                'color': '#ffa58e',
                'start': '2024-04-09' + 'T12:00:00',
                'end': '2024-04-09' + 'T15:00:00'
            }
        ]