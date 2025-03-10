import csv
titanic = []

with open("train.csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    titanic.append(linha)

# print(titanic[0])
# print(titanic[0]['Name'])

def titulo(texto):
  print()
  print(texto)
  print("-"*40)

def analise_sexo():
  titulo("Análise por Sexo")

  masc = 0
  fem = 0

  for pessoa in titanic:
    if pessoa['Sex'] == "male":
      masc += 1
    elif pessoa['Sex'] == "female":
      fem += 1
  
  # ----- outra forma (list comprehension)
  masc_sobre = len([pessoa for pessoa in titanic 
                if pessoa['Sex'] == "male" and pessoa['Survived'] == '1'])
  fem_sobre = len([pessoa for pessoa in titanic 
               if pessoa['Sex'] == "female" and pessoa['Survived'] == '1'])

  print(f"Homens: {masc}")
  print(f" - Sobreviventes: {masc_sobre}")
  print(f" - Mortos: {masc-masc_sobre}")
  print()
  print(f"Mulheres: {fem}")
  print(f" - Sobreviventes: {fem_sobre}")
  print(f" - Mortos: {fem - fem_sobre}")

def top10_idosos():
  titulo("Passageiros mais idosos - Top 10")

  titanic_temp = [x for x in titanic if x['Age'] != '']
  titanic2 = sorted(titanic_temp, key=lambda pessoa: float(pessoa['Age']), 
                    reverse=True)

  print("Nº Nome do Passageiro...............................: Idade Sobrevivente")
  
  # for x, pessoa in enumerate(titanic2, start=1):
  #   print(f"{x:2d} {pessoa['Name']:50s} {pessoa['Age']:5s} {'Sim' if pessoa['Survived'] == '1' else 'Não'}")
  #   if x == 10:
  #     break

  for x, pessoa in enumerate(titanic2[0:10], start=1):
    print(f"{x:2d} {pessoa['Name']:50s} {pessoa['Age']:5s} {'Sim' if pessoa['Survived'] == '1' else 'Não'}")
  

def analise_classe():
  pass

while True:
  titulo("Passageiros do Titanic: Exemplos de Análises")
  print("1. Análise por Sexo")
  print("2. Top 10 + idosos")
  print("3. Análise por Classe")
  print("4. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    analise_sexo()
  elif opcao == 2:
    top10_idosos()
  elif opcao == 3:
    analise_classe()
  else:
    break
