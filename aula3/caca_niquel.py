import time
import random

nome = input("Nome do Apostador: ")
valor = float(input("Valor R$: "))

input("Pressione Enter para iniciar o sorteio...")

figuras = "🍅🌷🌲"
jogo = ""

print("Suas apostas: ", end="")

for _ in range(3):
  num = random.randint(0, 2)
  print(figuras[num], end=" ", flush=True)
  time.sleep(1)
  jogo = jogo + figuras[num]

print()

if jogo[0] == jogo[1] and jogo[0] == jogo[2]:
  print(f"Parabéns {nome} 🎉🎉, você ganhou: {valor*3:.2f}")
elif jogo[0] == jogo[1] or jogo[0] == jogo[2] or jogo[1] == jogo[2]:
  print("Bah... quase! Siga tentando... 💣💣")
else:
  print("Não foi desta vez! 🤪🤪")