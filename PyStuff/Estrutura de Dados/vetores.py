class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho

    def inserir_elemento_posicao(self, elemento, posicao):
        self.__elementos[posicao] = elemento

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]