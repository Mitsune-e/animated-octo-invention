from pedidos_sys import main as pedidosSys
from cardapio_sys import criar_base_cardapio 
from cardapio_sys import listar_cardapio
from cliente_sys import main as cliente_sys

if __name__ == "__main__":
    # Inicio do programa, janela de opções
    criar_base_cardapio()
    while True:
        print("=============================================")
        print("Bem Vindo ao Coffee Shops Tia Rosa!")
        print("1 - Sistema de Pedidos")
        print("2 - Cardapio")
        print("3 - Listar Clientes")
        print("4 - Sair")
        option = int(input("Escolha uma opção: "))
        if option == 1:
            print("Sistema de Pedidos")
            pedidosSys()
        elif option == 2:
            listar_cardapio()
        elif option == 3:
            cliente_sys()
        elif option == 4:
            print("Saindo do sistema...")
            break
    