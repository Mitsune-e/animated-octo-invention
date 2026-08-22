from classes import pedido
from cardapio_sys import listar_cardapio
from cardapio_sys import buscar_item_cardapio_id
pedidos = []

def main():
    # Opções do sistema de pedidos controlado por input numerico
    while True:
        print("Bem vindo ao Sistema de Pedidos")
        print("1 - Adicionar Pedido")
        print("2 - Listar Pedidos")
        print("3 - Finalizar Pedido")
        print("4 - Voltar")       
        option = int(input("Escolha uma opção: "))
        if option == 1:
            adicionar_pedido()   
        elif option == 2:
            listar_pedidos()
        elif option == 3:
            finalizar_pedido()
        elif option == 4:
            print("Voltando para tela inicial...")
            break

def adicionar_pedido():
    #Adiciona um pedido a lista de pedidos, solicitando o nome do cliente e o item do cardapio
    cliente = input("Digite o nome do cliente: ")
    ver_cardapio = "s"
    ver_cardapio = input("Deseja ver cardapio? (s/n): ")
    if ver_cardapio.lower() == "s":  
        listar_cardapio()
    item_digitado = input("Digite o numero do item: ")
    item_pedido = buscar_item_cardapio_id(item_digitado)
    if item_pedido is None:
        print("Item não encontrado no cardápio.")
        input("Pressione qualquer tecla para continuar...")
        return
    pedidos.append(pedido.Pedido(cliente, item_pedido.nome, item_pedido.preco))

def listar_pedidos():
    #Lista todos os pedidos registrados, mostrando o nome do cliente, o item pedido, o preço e o status do pedido
    if not pedidos:
        print("Nenhum pedido registrado.")
        return None
    else:
        print("Pedidos Registrados:")
        for i, pedido in enumerate(pedidos, start=1):
            print(f"{i}. Cliente: {pedido.nome_cliente}, Pedido: {pedido.item_pedido}, Preço: R$ {pedido.preco:.2f}, Status: {pedido.status}")
        input("Pressione qualquer tecla para continuar...")

def finalizar_pedido():
    #Finaliza um pedido, alterando o status do pedido para "Finalizado"
    if not pedidos:
        print("Nenhum pedido registrado.")
    else:
        listar_pedidos()
        index = int(input("Digite o número do pedido que deseja finalizar: ")) - 1
        if 0 <= index < len(pedidos):
            pedidos[index].status = "Finalizado"
            print(f"Pedido de {pedidos[index].nome_cliente} finalizado: {pedidos[index].item_pedido}")
        else:
            print("Índice inválido. Nenhum pedido finalizado.")

def buscar_pedidos():
    #Retorna a lista de pedidos registrados
    return pedidos

if __name__ == "__main__":
    main()
