import requests
import matplotlib.pyplot as plt
from datetime import date, timedelta

url = "http://localhost:3000/"

def lista():
  titulo("Lista das Candidatas")

  response = requests.get(url + "candidatas")

  if response.status_code != 200:
    print("Erro... Não foi possível acessar a API")
    return
  
  candidatas = response.json()

  print("Nº Nome...............: Clube.........: Idade: Sonho.............................:")
  print("----------------------------------------------------------------------------------")

  for cand in candidatas:
    print(f"{cand['id']:2d} {cand['nome']:20s} {cand['clube']:15s} {cand['idade']:2d}anos {cand['sonho'] if len(cand['sonho']) <= 35 else cand['sonho'][0:32]+"..."}")


def votar():
  lista()

  titulo("Inclusão de Votos", "=")

  codigo = int(input("Nº da Candidata..: "))
  
  response = requests.get(url + "candidatas")
  candidatas = response.json()
  escolhida = [x for x in candidatas if x['id'] == codigo]
  if (len(escolhida) == 0):
    print("Número inválido")
    return
  print(f"Nome da Candidata: {escolhida[0]['nome']}")  
  print(f"Clube............: {escolhida[0]['clube']}")  

  justificativa = input("Justificativa....: ")
  data          = input("Data.............: ")

  voto = {
    "clienteId": 1,
    "candidataId": codigo
  }

  if justificativa:
    voto.update({"justificativa": justificativa})

  if data:
    voto.update({"data": data})

  response = requests.post(url+"votos", json=voto)

  if response.status_code == 201:
    incluido = response.json()
    print(f"Ok! Voto cadastrado com código: {incluido['voto']['id']}")
  else:
    print("Erro... Não foi possível incluir o voto")  


def resultado():
  titulo("Resultado Parcial: Rainha da Fenadoce")

  response = requests.get(url + "candidatas")

  if response.status_code != 200:
    print("Erro... Não foi possível acessar a API")
    return
  
  candidatas = response.json()
  candidatas2 = sorted(candidatas, key=lambda cand: cand['numVotos'], reverse=True)

  print("Nº Nome...............: Clube.........: Votos")
  print("-----------------------------------------------")

  for cand in candidatas2:
    print(f"{cand['id']:2d} {cand['nome']:20s} {cand['clube']:15s} {cand['numVotos']:4d}")


def graf_colunas():
  response = requests.get(url+"candidatas")

  if response.status_code != 200:
    print("Erro... Não foi possível acessar a API")
    return

  candidatas = response.json()

  fig, ax = plt.subplots(figsize=(9, 5))

  nomes = [str(x['id'])+"-"+x['nome'].split(" ")[0] for x in candidatas]
  votos = [x['numVotos'] for x in candidatas]
  bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:cyan', 'tab:purple', 'tab:pink', 'tab:brown']

  ax.bar(nomes, votos, color=bar_colors)

  ax.set_ylabel('Nº Votos')
  ax.set_title('Resultado Parcial do Concurso')
  plt.gcf().canvas.manager.set_window_title("Gráfico com Resultado Parcial")
  plt.xticks(rotation=10)
  plt.show()

def formata_data(data):
  # recebe a data como "2024-11-02" e devolve "02/11"
  return data[8:10] + "/" + data[5:7]

def graf_linhas():
  response = requests.get(url+"votos")

  if response.status_code != 200:
    print("Erro... Não foi possível acessar a API")
    return
  
  todos_votos = response.json()
  # print(todos_votos[0])    
  # data_atual = date.today()  
  # print(data_atual)
  # data_1 = date.today() - timedelta(days=9)
  # print(data_1)   

  votos = []
  dias = []

  for i in range(10):
    data = str(date.today() - timedelta(days=9-i))
    dias.append(formata_data(data))
    votos.append(len([x for x in todos_votos if str(x['data']).startswith(str(data))]))

  # print(dias)
  # print(votos)
  plt.figure(figsize=(9, 5))
  plt.plot(dias, votos, label="Nº Votos")
  plt.title("Evolução dos Votos por Dia (últimos 10 dias)")
  plt.legend()
  plt.gcf().canvas.manager.set_window_title("Gráfico de Votos")
  plt.show()

def titulo(texto, traco="-"):
  print()
  print(texto)
  print(traco*40)

# ---------------------------- Programa Principal
while True:
  titulo("Rainha da Fenadoce")
  print("1. Lista das Candidatas")
  print("2. Votar")
  print("3. Resultado Parcial")
  print("4. Gráfico de Colunas")
  print("5. Gráfico de Linhas")
  print("6. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    lista()
  elif opcao == 2:
    votar()
  elif opcao == 3:
    resultado()
  elif opcao == 4:
    graf_colunas()
  elif opcao == 5:
    graf_linhas()
  else:
    break