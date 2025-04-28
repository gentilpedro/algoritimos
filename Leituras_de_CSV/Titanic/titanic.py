import csv

titanic = []

with open('titanic.csv', mode = 'r') as file:
    dados_csv = csv.DictReader(file)
    for linha in dados_csv:
        titanic.append(linha)

def titulo(mensa, troco ="-"):
    print()
    print(mensa.upper())
    print(troco*50)

def dados_por_sexo_sobreviventes():
    titulo("Dados por Sexo e Sobreviventes")
    print("Sexo\tSobreviventes")
    print("-"*50)


def dados_por_idade():
    titulo("Dados por Idade e + 10 idosos")
    print("Idade\tSobreviventes")
    print("-"*50)

def dados_por_classe_sobreviventes():
    titulo("Dados por Classe e Sobreviventes")
    print("Classe\tSobreviventes")
    print("-"*50)

while True:
    titulo("Menu Principal")
    print("1 - Dados por Sexo e sobreviventes")
    print("2 - Medias de Idade e + 10 idosos")
    print("3 - Dados por classe e Sobreviventes")
    print("4 - Finalizar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        dados_por_sexo_sobreviventes()

    elif opcao == "2":
        dados_por_idade()

    elif opcao == "3":
        dados_por_classe_sobreviventes()
    elif opcao == "4":
        titulo("Finalizando")
        print("Obrigado por usar o programa!")
        break