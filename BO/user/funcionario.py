import model.user.funcionario
from BO.base.decorators import Response

class Funcionario:
    def __init__(self):
        pass

    @Response(desc_error='Erro ao buscar funcionarios', lista_retornos=['lista_funcionarios'])
    def buscar_funcionarios(self):
        return model.user.funcionario.FuncionarioModel().buscar_funcionarios_combo()
