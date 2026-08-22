from classes import iten_cardapio

cardapio = []

def main():
    print("a")

def criar_base_cardapio():
    #Cria uma base de cardápio com itens predefinidos
    cardapio.append(iten_cardapio.Item("Café Expresso", 5.00))
    cardapio.append(iten_cardapio.Item("Cappuccino", 7.50))
    cardapio.append(iten_cardapio.Item("Latte", 6.50))
    cardapio.append(iten_cardapio.Item("Mocha", 8.00))
    cardapio.append(iten_cardapio.Item("Chá Gelado", 4.00))
    cardapio.append(iten_cardapio.Item("Suco Natural", 6.00))
    cardapio.append(iten_cardapio.Item("Bolo de Chocolate", 10.00))
    cardapio.append(iten_cardapio.Item("Torta de Limão", 12.00))
    cardapio.append(iten_cardapio.Item("Sanduíche Natural", 15.00))

def listar_cardapio():
    #Lista todos os itens do cardápio, mostrando o ID, nome e preço
    if not cardapio:
        print("Nenhum item no cardápio.")
    else:
        print("Cardápio:")
        for item in cardapio:
            print(f"ID: {item.id}, Nome: {item.nome}, Preço: R${item.preco:.2f}")
        input("Pressione qualquer tecla para continuar...")

def buscar_item_cardapio_id(id):
    #Busca um item do cardápio pelo ID e retorna o item correspondente
    id = int(id)  # Converte o ID para inteiro
    for item in cardapio:
        if item.id == id:
            return item
    return None

if __name__ == "__main__":
    main()