from array import array
from vetores import Vetor 

""" vetor_inteiros = array("b", [1,2 ,3 ])
print(vetor_inteiros)

vetor_inteiros.insert(3,4)
print(vetor_inteiros)


print(vetor_inteiros.index(2)) """

print(30 * "-", "Menu", 30 * "-")
print("1 - Vetores")
print("2 - Listas Ligadas")

menu = int (input("Escolha uma opção: "))

if menu == 1:
    vetor_teste = Vetor(3)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(3, 1)
    print(vetor_teste.listar_elemento(0))
    print(vetor_teste.listar_elemento(1))