from model.base.sql import SQLConexao


class Cliente(SQLConexao):

    def __init__(self):
        super().__init__()

    def buscar_clientes(self):
        return self.select(query=f"""
            SELECT id, nm_completo 
            FROM {self.schema_cliente}.cliente
            WHERE status
            ORDER BY nm_completo
        """)