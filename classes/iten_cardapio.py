import itertools

class Item:
    #Classe que representa um item do cardápio, contendo informações sobre o nome do item e o preço.
    _id_iter = itertools.count(start=1)
    def __init__(self, nome, preco):
        self.id = next(self._id_iter)  # Gera um ID único para o item
        self.nome = nome
        self.preco = preco

    