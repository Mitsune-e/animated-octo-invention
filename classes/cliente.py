class Cliente:
    def __init__(self, nome):
        #Classe que representa um cliente, contendo informações sobre o nome do cliente, o número de visitas e os pontos de fidelidade.
        self.nome = nome
        self.vezes_visitas = 1
        self.pontos_fidelidade = 10