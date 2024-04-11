from BO.base.decorators import Response
from model.user.sessao import SessaoModel


class Sessao:
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.matricula = None
        self.lista_ponto_funcao = None
        self.grupos = []
        self.lista_grupos = []
        self.grupo_principal = None
        self.usuario = None
        self.tela_principal = None
        self.__fazer()

    @Response(desc_error='Erro ao buscar sessão do usuario', is_manter_retorno=True)
    def get_sessao(self):
        return {
            'matricula': self.usuario['matricula'],
            'lista_ponto_funcao': self.lista_ponto_funcao,
            'grupos': self.grupos,
            'usuario': self.usuario,
            'tela_principal': self.tela_principal
        }

    @Response(desc_error='Erro em buscar matricula')
    def __get_matricula(self):
        self.matricula = self.usuario['matricula']

    @Response(desc_error='Erro em fazer sessao')
    def __fazer(self):
        self.__get_usuario()
        self.__get_matricula()
        self.__get_pontofucao()
        self.__get_grupos()
        self.__tela_principal()

    @Response(desc_error='Erro ao buscar informacoes do usuario')
    def __get_usuario(self):
        self.usuario = SessaoModel().get_usuario(user_id=self.user_id)

    @Response(desc_error='Erro ao buscar permissoes do usuario')
    def __get_pontofucao(self):
        self.lista_ponto_funcao = SessaoModel().get_pontofuncao_user(matricula=self.matricula)

    @Response(desc_error='Erro ao buscar grupos do usuario')
    def __get_grupos(self):
        self.lista_grupos = SessaoModel().get_grupos_user(matricula=self.matricula)
        if not self.lista_grupos:
            self.grupos = []
            return

        for grupo in self.lista_grupos:
            self.grupos.append(grupo.get('grupo_id'))

    @Response(desc_error='Erro ao buscar grupo principal')
    def __get_grupo_princpal(self):
        if not self.lista_grupos:
            return
        self.grupo_principal = self.lista_grupos[0]['nome']

    @Response(desc_error='Erro ao buscar tela principal')
    def __tela_principal(self):
        if not self.lista_grupos:
            return
        self.tela_principal = self.lista_grupos[0]['tela_principal']

