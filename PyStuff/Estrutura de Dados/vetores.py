class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho

    def inserir_elemento_posicao(self, elemento, posicao):
        self.__elementos[posicao] = elemento

    def inserir_elemento_final(self, elemento):
        for i in range(self.__tamanho):
            if self.__elementos[i] is None:
                self.__elementos[i] = elemento
                return
        raise Exception("Vetor cheio")
    
    
    def listar_elemento(self, posicao):
        return self.__elementos[posicao]