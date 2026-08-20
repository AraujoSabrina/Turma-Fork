alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    print("\n--- ALUNOS Inserindo---")
    print("Modificacao")
    if not alunos:
        print("Nenhum aluno cadastrado tesr.")
    for aluno in alunos:
        print(aluno)
    print()
    print("Número de alunos: " + str(len(alunos)))

def exclusao():
    nome = input("Digite o nome do aluno: ")
    alunos.remove(nome)
    print("Aluno removido com sucesso!")


def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")
    encontrados = [aluno for aluno in alunos if nome_busca.lower() in aluno.lower()]
    
    print("\n--- RESULTADO DA BUSCA ---")
    if encontrados:
        for aluno in encontrados:
            print(f"Aluno encontrado: {aluno}")
    else:
        print("Nenhum aluno encontrado com esse nome.")

while True:
    print("\n1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_aluno()



    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        buscar_aluno()

    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")