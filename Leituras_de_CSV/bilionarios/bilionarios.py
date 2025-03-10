import csv
bils = []

with open("Billionaires Statistics Dataset.csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    bils.append(linha)

def titulo(texto):
  print()
  print(texto)
  print("-"*40)

def top20():
  titulo("Top 20: Maiores Bilionários")

  print("Nº Nome..............................: País..........: Categoria..........: Fortuna U$:")

  for x, bil in enumerate(bils[0:20], start=1):
    print(f"{x:2d} {bil['personName']:35s} {bil['country']:15s} {bil['category']:20s} {bil['finalWorth']}")

def compara():
  # Ler o nome de 2 países
  # Exibir nome, categoria e idade dos bilionários de cada um destes países
  # No final, exibir a quantidade de bilionários de cada país
  titulo("Compara Bilionários de 2 países")

  pais1 = input("1º País: ").upper()
  pais2 = input("2º País: ").upper()

  print(f"\nBilionários: {pais1}")
  print("-"*40)
  
  num1 = 0
  for bil in bils:
    if bil['country'].upper() == pais1:
      print(bil['personName'])
      num1 += 1

  print(f"\nBilionários: {pais2}")
  print("-"*40)
  
  num2 = 0
  for bil in bils:
    if bil['country'].upper() == pais2:
      print(bil['personName'])
      num2 += 1

  print(f"\nTotal {pais1}: {num1}")
  print(f"Total {pais2}: {num2}")

def agrupa_categoria():
  titulo("Agrupar Bilionários por Categorias")

  categorias = list(set([x['category'] for x in bils]))
  numeros = [0] * len(categorias)

  for bil in bils:
    indice = categorias.index(bil['category'])
    numeros[indice] += 1

  juntos = sorted(zip(numeros, categorias), reverse=True)

  for num, cat in juntos:
    print(f"{cat} - {num} bilionários")

def agrupa_pais():
  titulo("Agrupar Bilionários por Países")

  paises = list(set([x['country'] for x in bils]))
  numeros = [0] * len(paises)

  for bil in bils:
    indice = paises.index(bil['country'])
    numeros[indice] += 1

  juntos = sorted(zip(numeros, paises), reverse=True)

  for x, (num, pais) in enumerate(juntos, start=1):
    print(f"{pais} - {num} bilionários")
    if (x % 20 == 0):
      input("... pressione enter para continuar ...")

while True:
  titulo("Lista de Bilionários: Análise dos Dados")
  print("1. Top 20 Bilionários")
  print("2. Comparar 2 Países")
  print("3. Agrupar por Categorias")
  print("4. Agrupar por Países")
  print("5. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    top20()
  elif opcao == 2:
    compara()
  elif opcao == 3:
    agrupa_categoria()
  elif opcao == 4:
    agrupa_pais()
  else:
    break
