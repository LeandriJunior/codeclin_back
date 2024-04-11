from BO.base.decorators import Response
from model.base.sql import SQLConexao


class FuncionarioModel(SQLConexao):
    def __init__(self):
        super().__init__()

    @Response(desc_error='Model: Erro ao buscar funcionarios', is_manter_retorno=True)
    def buscar_funcionarios_combo(self):
        return self.select(query=f"""
            SELECT matricula, nm_completo 
            FROM {self.schema_cliente}.funcionario
            WHERE status
            ORDER BY nm_completo  
        """)
