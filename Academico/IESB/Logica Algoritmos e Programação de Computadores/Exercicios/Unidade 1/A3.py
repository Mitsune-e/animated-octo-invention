def main():
    print("Bem-vindo ao sistema de consultas veterinárias!")
    print(str(len(lista_consultas))+" Consultas registradas")
    print("1.Adicionar Consulta")
    print("2.Listar Consultas")
    print("3.Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_consulta(input("Digite o nome do tutor: "), input("Digite o nome do animal: "), input("Digite a idade do animal: "), input("Digite o motivo da consulta: "))
    elif opcao == "2":
        listar_consultas()
    elif opcao == "3":
        print("Saindo do sistema...")
        global running
        running = False

def adicionar_consulta(tutor, nome_animal, idade_animal, motivo_consulta):
    consulta = {
        "tutor": tutor,
        "nome_animal": nome_animal,
        "idade_animal": idade_animal,
        "motivo_consulta": motivo_consulta
    }
    lista_consultas.append(consulta)
def listar_consultas():
    if len(lista_consultas) == 0:
        print("Nenhuma consulta cadastrada.")
    else:
        for i, consulta in enumerate(lista_consultas):
            print("=============================================")
            print(f"Consulta {i+1}:")
            print(f"Tutor: {consulta['tutor']}")
            print(f"Nome do Animal: {consulta['nome_animal']}")
            print(f"Idade do Animal: {consulta['idade_animal']}")
            print(f"Motivo da Consulta: {consulta['motivo_consulta']}")
            print("=============================================")

if __name__ == "__main__":
    lista_consultas = []
    running = True
    while ( running ):
        main()
