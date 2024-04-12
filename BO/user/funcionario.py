import model.user.funcionario
from BO.base.decorators import Response
from BO.base.excecao import ValidationError


class Funcionario:
    def __init__(self):
        pass

    @Response(desc_error='Erro ao buscar funcionarios', lista_retornos=['lista_funcionarios'])
    def buscar_funcionarios(self):
        return model.user.funcionario.FuncionarioModel().buscar_funcionarios_combo()

    @Response(desc_error='Erro ao pesquisar funcionarios', lista_retornos=['lista_funcionarios'])
    def buscar_funcionarios_pesquisa(self, pesquisa=None):
        if not pesquisa:
            raise ValidationError('precisar pesquisar algo para encontrar funcionario')
        funcionarios = model.user.funcionario.FuncionarioModel().buscar_funcionarios_pesquisa(pesquisa=pesquisa)

        if not funcionarios:
            raise ValidationError('Nenhum funcionario encontrado')

        return funcionarios
