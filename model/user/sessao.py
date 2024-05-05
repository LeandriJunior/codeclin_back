from BO.base.decorators import Response
from model.base.sql import SQLConexao


class SessaoModel(SQLConexao):
    def __init__(self):
        super().__init__()

    @Response(desc_error='Model: Erro ao buscar informacoes do usuario', is_manter_retorno=True)
    def get_usuario(self, user_id=None):
        return self.select(
            query=f"""
                    SELECT  f.matricula, f.status , f.nm_completo, f.nm_primeiro, f.nm_ultimo, f.cpf, f.cpf_form,
                            f.funcionario_responsavel_id, f.cargo_id, f.user_id, f.email,
                            TO_CHAR(f.dat_nasc, 'YYYYMMDD') AS dat_nasc
                    FROM {self.schema_cliente}.funcionario f
                    LEFT JOIN {self.schema_cliente}.user u ON u.id = f.user_id
                    WHERE f.user_id = :user_id;
                """,
            parametros={'user_id': user_id},
            is_primeiro=True
        )

    @Response(desc_error='Model: Erro ao buscar permissões do usuario', is_manter_retorno=True)
    def get_pontofuncao_user(self, matricula=None):
        return self.select(query=f"""
                SELECT ponto_funcao_id FROM {self.schema_cliente}.funcionario_perfilpontofuncao upp
                INNER JOIN {self.schema_cliente}.funcionario_perfilfuncionario upu ON upu.perfil_id = upp.perfil_id
                WHERE upu.funcionario_id = :matricula AND upp.status = true """,
            parametros={'matricula': matricula},
            is_values_list=True)

    def get_grupos_user(self, matricula=None):
        return self.select(query=f"""
                SELECT usu.grupo_id, usu.tela_principal, us.nome
                FROM {self.schema_cliente}.funcionario_grupofuncionario usu
                INNER JOIN {self.schema_cliente}.funcionario_grupo us ON us.nome = usu.grupo_id
                WHERE funcionario_id = :matricula order by us.nivel;""",
            parametros={'matricula': matricula})


