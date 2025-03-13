import random
import time
import os
from colorama import Fore, Back, Style

temp = "🐶🐶🐵🐵🐯🐯🐸🐸🐪🐪🐢🐢🐟🐟🐞🐞"
figuras = list(temp)

jogo = []
memoria = []

print("Jogo da Memória")
print("-"*30)
nome = input("Nome do Jogador: ")
pontos = 0
# acertos += 10
# erros -= 5
hora_inicial = time.time()

def preenche_matriz():
  for i in range(4):
    jogo.append([])
    memoria.append([])
    for _ in range(4):
      num = random.randint(0, len(figuras)-1)
      jogo[i].append(figuras[num])
      memoria[i].append("🟥")
      figuras.pop(num)

def mostra_tabuleiro():
  os.system("clear")
  print("   1   2   3   4")
  for i in range(4):
    print(f"{i+1}", end="")
    for j in range(4):
      print(f" {jogo[i][j]} ", end="")
    print("\n")

  print("Memorize a posição dos bichos... Vamos testar sua Memória!")
  time.sleep(2)

  print("Contagem Regressiva: ", end="")
  for i in range(10, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)

def mostra_memoria():
  os.system("clear")
  print("   1   2   3   4")
  for i in range(4):
    print(f"{i+1}", end="")
    for j in range(4):
      print(f" {memoria[i][j]} ", end="")
    print("\n")

def faz_aposta(num):
  while True:
    mostra_memoria()
    aposta = input(f"{num}ª Coordenada (2 números: linha e coluna): ")
    if len(aposta) != 2:
      print("Digite uma dezena, como 12, 24, 31, 43...")
      time.sleep(2)
      continue
    x = int(aposta[0])-1
    y = int(aposta[1])-1
    try:
      if memoria[x][y] == "🟥":
        memoria[x][y] = jogo[x][y]
        break
      else:
        print("Coordenada já apostada... digite novamente")
        time.sleep(2)
    except IndexError:
      print("Coordenada inválida... digite novamente")
      time.sleep(2)
  return (x, y)

def verifica_tabuleiro():
  faltam = 0
  for i in range(4):
    for j in range(4):
      if memoria[i][j] == "🟥":
        faltam += 1
  return faltam

preenche_matriz()
mostra_tabuleiro()

while True:
  x1, y1 = faz_aposta(1)
  x2, y2 = faz_aposta(2)
  mostra_memoria()

  if memoria[x1][y1] == memoria[x2][y2]:
    print("Aeee, você acertou")
    contador = verifica_tabuleiro()
    pontos += 10
    if contador == 0:
      print("Parabéns! Você venceu! 🏆🏆")
      break
    else:
      print(f"Falta(m) {contador//2} bicho(s) para descobrir a posição")
      time.sleep(3)
  else:
    print("Ops... você errou")
    pontos -= 5

    memoria[x1][y1] = "🟥"
    memoria[x2][y2] = "🟥"

    sair = input("Desistir (S/N)? ").upper()
    if sair == "S":
      break

hora_final = time.time()
duracao = hora_final - hora_inicial

print("-"*40)
print(f"{nome}, você fez um total de {pontos} pontos")
print(f"Duração do Jogo: {duracao:.3f} segundos")

# grava os dados do jogador no arquivo de rankings
dados = []
if os.path.isfile("ranking.txt"):
  with open("ranking.txt", "r") as arq:
    dados = arq.readlines()
dados.append(f"{nome};{pontos};{duracao:.3f}\n")

with open("ranking.txt", "w") as arq:
  for linha in dados:
    arq.write(linha)

# Processo para classificar (ordenar) os jogadores
# com maior pontuação (e, se igual, por menor tempo)
jogadores = []
pontuacoes = []
tempos = []

for linha in dados:
  partes = linha.split(";")
  jogadores.append(partes[0])
  pontuacoes.append(int(partes[1]))
  tempos.append(float(partes[2])*-1)

juntos = sorted(zip(pontuacoes, tempos, jogadores), reverse=True)
pontuacoes2, tempos2, jogadores2 = zip(*juntos)

input("Pressione Enter para ver o Ranking...")
os.system("cls")
print("Ranking dos Jogadores da Memória")
print("-----------------------------------------------------")
print("Nº Nome do Jogador..............: Pontos Tempo......:")

for pos, (jogador, ponto, tempo) in enumerate(zip(jogadores2, pontuacoes2, tempos2), start=1):
  if jogador == nome:
    print(Fore.RED+f"{pos:2d} {jogador:30s}   {ponto:2d}   {tempo*-1:7.3f} seg.", end="")
    print(Style.RESET_ALL)
  else:
    print(f"{pos:2d} {jogador:30s}   {ponto:2d}   {tempo*-1:7.3f} seg.")