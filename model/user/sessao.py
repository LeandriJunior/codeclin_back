from BO.base.decorators import Response
from model.base.sql import SQLConexao


class SessaoModel(SQLConexao):
    def __init__(self):
        super().__init__()

    @Response(desc_error='Model: Erro ao buscar informacoes do usuario', is_manter_retorno=True)
    def get_usuario(self, usuario_id=None):
        return self.select(
            query=f"""
                    SELECT nm_primeiro, nm_ultimo 
                    FROM {self.schema_cliente}.user 
                    WHERE id = :usuario_id
                """,
            parametros={'usuario_id': usuario_id}
        )

    @Response(desc_error='Model: Erro ao buscar permissões do usuario', is_manter_retorno=True)
    def get_pontofuncao_user(self, usuario_id=None):
        return self.select(query=f"""
                SELECT ponto_funcao_id FROM {self.schema_cliente}.user_perfil_pontofuncao upp
                INNER JOIN {self.schema_cliente}.user_perfil_user upu ON upu.perfil_id = upp.perfil_id
                WHERE upu.usuario_id = :usuario_id AND upp.status = true """,
            parametros={'usuario_id': usuario_id},
            is_values_list=True)

    def get_grupos_user(self, usuario_id=None):
        return self.select(query=f"""
                SELECT grupo_id, tela_principal FROM {self.schema_cliente}.user_grupo_user usu
                INNER JOIN {self.schema_cliente}.user_grupo us ON us.nome = usu.grupo_id
                WHERE usuario_id = :usuario_id order by us.nivel;""",
            parametros={'usuario_id': usuario_id})


