import itertools

class Pedido:
    #Classe que representa um pedido feito por um cliente, contendo informações sobre o cliente, o item pedido, o status do pedido e o preço.
    _id_iter = itertools.count(start=1)
    def __init__(self, nome_cliente, item_pedido, item_preco):
        self.id = next(self._id_iter)  # Gera um ID único para o pedido
        self.nome_cliente = nome_cliente
        self.item_pedido = item_pedido
        self.status = "Em andamento"
        self.preco = item_preco