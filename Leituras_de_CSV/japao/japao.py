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