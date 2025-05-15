import csv

formula1 = []

with open("winners.csv", mode="r") as arq:
    winners = csv.DictReader(arq)
    for linha in winners:
        formula1.append(linha)


def titulo(texto):
    print()
    print(texto)
    print("-" * 40)


def top10_pilotos():
    pass


def equipe10vitorias():
    pass


def top10_corridas():
    pass


def pilotoAnos():
    titulo("Anos de Vitorias de um Piloto")
    piloto = input("Digite o nome do piloto: ").upper()

    anos = set()

    for corrida in formula1:
        if corrida['Winner'].upper() == piloto:
            anos.add(corrida['Date'][0:4])

    if len(anos) > 0:
        anos2 = sorted(list(anos))
        print(f"{piloto} venceu corridas nos anos de:")
        print(",".join(anos2))
        print("-" * 30)
        print(f"{piloto} venceu corridas nos anos em {len(anos2)}")
    else:
        print(f"Piloto nao venceu corridas")


def anos_vitoria():
    pass


# -------------------------------- Programa Principal
while True:
    titulo("Dados de corridas de Formula 1")
    print("1. Top 10 Pilotos + Vitoriosos")
    print("2. Equipes com 10 ou + Vitorias")
    print("3. Top 10 Corridas mais longas")
    print("4. Piloto e anos de vitoria")
    print("5. Vitoria e ano de vitoria")
    print("5. Finalize")

    opcao = int(input("Opção: "))
    if opcao == 1:
        top10_pilotos()
    elif opcao == 2:
        equipe10vitorias()
    elif opcao == 3:
        top10_corridas()
    elif opcao == 4:
        pilotoAnos()
    elif opcao == 5:
        anos_vitoria()
    else:
        break
