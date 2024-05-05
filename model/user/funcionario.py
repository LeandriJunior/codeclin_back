from model.base.sql import SQLConexao


class FuncionarioModel(SQLConexao):
    def __init__(self):
        super().__init__()

    def buscar_funcionarios_combo(self, funcionario_id=None, is_primeiro=False):
        condicao = 'status'
        if funcionario_id:
            condicao += ' AND matricula = :funcionario_id'

        return self.select(query=f"""
                    SELECT matricula, nm_completo 
                    FROM {self.schema_cliente}.funcionario
                    WHERE {condicao}
                    ORDER BY nm_completo  
                """,
            is_primeiro=is_primeiro,
            parametros={'funcionario_id': funcionario_id})

    def buscar_funcionarios_pesquisa(self, pesquisa=None):
        return self.select(query=f"""
                    SELECT matricula, nm_completo 
                    FROM {self.schema_cliente}.funcionario
                    WHERE status AND nm_completo ILIKE '%{pesquisa}%'
                    ORDER BY nm_completo  
                """)
