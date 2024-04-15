import model.user.cliente
from BO.base.decorators import Response


class Cliente:

    @Response(desc_error="Erro ao buscar clientes", lista_retornos=['lista_clientes'])
    def buscar_clientes(self):
        return model.user.cliente.Cliente().buscar_clientes()