from classes import cliente
from pedidos_sys import buscar_pedidos

def main():
    print("Sistema de Clientes:")
    listar_clientes()

def listar_clientes():
    #Lista todos os clientes registrados, mostrando o nome do cliente, o número de visitas e os pontos de fidelidade
    pedidos = buscar_pedidos()
    if pedidos is None:
        print("Nenhum cliente achado.")
    todos_clientes = []
    nomes_clientes = []
    for i in range(len(pedidos)):
        novo_cliente = cliente.Cliente(pedidos[i].nome_cliente)
        if novo_cliente.nome not in nomes_clientes:
            todos_clientes.append(novo_cliente)
            nomes_clientes.append(novo_cliente.nome)
        else:
            for item in todos_clientes:
                if item.nome == novo_cliente.nome:
                    item.vezes_visitas += 1
                    item.pontos_fidelidade += 10
            break
            
    print("Clientes Listados:")
    for i in range(len(todos_clientes)):
        print(f"{i+1}. Nome: {todos_clientes[i].nome}, Visitas: {todos_clientes[i].vezes_visitas}, Pontos de Fidelidade: {todos_clientes[i].pontos_fidelidade}")    
    input("Pressione qualquer tecla para continuar...")
