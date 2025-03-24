import time;
import random;

nome = input("Qual o nome do apostador: ")

valor = float(input("Qual o valor da aposta: "))
input("Pressione enter para começar o sorteio")

figuras = "🍓 🥝 🍑"
jogo = ""

print ("Suas apostas: ", end="")

for _ in range(3):
    ##Gera um numero aleatorio entre 0.. 2
    num = random.randint(0, 2)
    print(figuras[num], end=" ", flush=True)
    time.sleep(1)
    jogo = jogo + figuras[num]
    
print()

if jogo[0] == jogo[1] and jogo[1] == jogo[2]:
    print(f"Parabéns {nome} você ganhou R$ {valor * 3:6.2}!")
elif jogo[0] == jogo[1] or jogo[1] == jogo[2] or jogo[1] == jogo[2]:
    print(f"Ah... foi quase {nome}, mais sorte na proxima vez!!")
else:
    print(f"Que pena {nome} você perdeu R$ {valor}")
    