from BO.base.decorators import Response
from model.user.sessao import SessaoModel


class Sessao:
    def __init__(self, usuario_id=None):
        self.usuario_id = usuario_id
        self.lista_ponto_funcao = None
        self.grupos = None
        self.lista_grupos = None
        self.grupo_principal = None
        self.usuario = None
        self.tela_principal = None
        self.__fazer()

    @Response(desc_error='Erro ao buscar sessão do usuario', lista_retornos=['sessao'])
    def get_sessao(self):
        return {
            'usuario_id': self.usuario_id,
            'lista_ponto_funcao': self.lista_ponto_funcao,
            'grupos': self.grupos,
            'usuario': self.usuario,
            'tela_principal': self.tela_principal
        }

    @Response(desc_error='Erro em fazer sessao')
    def __fazer(self):
        self.__get_usuario()
        self.__get_pontofucao()
        self.__get_grupos()
        self.__tela_principal()

    @Response(desc_error='Erro ao buscar informacoes do usuario')
    def __get_usuario(self):
        self.usuario = SessaoModel().get_usuario(usuario_id=self.usuario_id)

    @Response(desc_error='Erro ao buscar permissoes do usuario')
    def __get_pontofucao(self):
        self.lista_ponto_funcao = SessaoModel().get_pontofuncao_user(usuario_id=self.usuario_id)

    @Response(desc_error='Erro ao buscar grupos do usuario')
    def __get_grupos(self):
        self.lista_grupos = SessaoModel().get_grupos_user(usuario_id=self.usuario_id)
        self.grupos = [grupo['grupo_id'] for grupo in self.lista_grupos]

    @Response(desc_error='Erro ao buscar grupo principal')
    def __get_grupo_princpal(self):
        self.grupo_principal = self.lista_grupos[0]['nome']

    @Response(desc_error='Erro ao buscar tela principal')
    def __tela_principal(self):
        self.tela_principal = self.lista_grupos[0]['tela_principal']

