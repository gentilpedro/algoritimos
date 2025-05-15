import random
import json
import os

# Função para criar o tabuleiro
def criar_tabuleiro():
    return [['🌊'] * 10 for _ in range(10)]

# Função para mostrar o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(linha))

# Função para posicionar navios no tabuleiro
def posicionar_navios(tabuleiro):
    navios = 4  # Número de navios
    for _ in range(navios):
        while True:
            try:
                linha = int(input("Escolha a linha (0-9): "))
                coluna = int(input("Escolha a coluna (0-9): "))
                if 0 <= linha < 10 and 0 <= coluna < 10:  # Valida os limites
                    if tabuleiro[linha][coluna] == '🌊':  # Verifica se já há navio
                        tabuleiro[linha][coluna] = '🚢'  # Marca o navio
                        break
                    else:
                        print("Essa posição já está ocupada!")
                else:
                    print("Posição fora do tabuleiro! Tente novamente.")
            except ValueError:
                print("Entrada inválida! Insira números inteiros.")


# Função para salvar o ranking no arquivo JSON
def salvar_ranking(nome, vitorias):
    if os.path.exists('ranking.json'):
        with open('ranking.json', 'r') as f:
            ranking = json.load(f)
    else:
        ranking = []

    encontrado = False
    for jogador in ranking:
        if jogador['nome'] == nome:
            jogador['vitorias'] += vitorias  # Incrementa as vitórias
            encontrado = True
            break

    if not encontrado:
        ranking.append({'nome': nome, 'vitorias': vitorias})

    ranking = sorted(ranking, key=lambda x: x['vitorias'], reverse=True)

    with open('ranking.json', 'w') as f:
        json.dump(ranking, f, indent=4)

# Função para carregar o ranking do arquivo JSON
def carregar_ranking():
    if os.path.exists('ranking.json'):
        with open('ranking.json', 'r') as f:
            return json.load(f)
    return []

# Função para mostrar o ranking
def mostrar_ranking():
    ranking = carregar_ranking()
    if ranking:
        print("\nRanking dos jogadores:")
        for i, jogador in enumerate(ranking, 1):
            print(f"{i}. {jogador['nome']} - Vitórias: {jogador['vitorias']}")
    else:
        print("\nNão há jogadores no ranking.")

# Função para jogar contra outro jogador
def jogar_contra_maquina():
    tabuleiro_player = criar_tabuleiro()
    tabuleiro_maquina = criar_tabuleiro()

    print("Insira seu nome:")
    nome_player = input()
    print(f"{nome_player}, posicione seus navios:")
    posicionar_navios(tabuleiro_player)

    for _ in range(4):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if tabuleiro_maquina[linha][coluna] == '🌊':
                tabuleiro_maquina[linha][coluna] = '🚢'
                break

    vez_do_jogador = True
    while True:
        if vez_do_jogador:
            print(f"\n{nome_player}, é sua vez!")
            mostrar_tabuleiro(tabuleiro_maquina)
            try:
                linha = int(input("Escolha a linha (0-9) para atacar: "))
                coluna = int(input("Escolha a coluna (0-9) para atacar: "))
                if 0 <= linha < 10 and 0 <= coluna < 10:
                    if tabuleiro_maquina[linha][coluna] == '🚢':
                        print("💥 Acertou um navio inimigo!")
                        tabuleiro_maquina[linha][coluna] = 'X'
                        if all(cell != '🚢' for row in tabuleiro_maquina for cell in row):
                            print(f"{nome_player} venceu!")
                            salvar_ranking(nome_player, 1)
                            break
                        continue  # Permanece a vez do jogador
                    elif tabuleiro_maquina[linha][coluna] == '🌊':
                        print("🌊 Errou!")
                        tabuleiro_maquina[linha][coluna] = 'O'
                        vez_do_jogador = False
                        os.system('clear')
                    else:
                        print("Você já atacou essa posição!")
                        continue
                else:
                    print("Posição fora do tabuleiro! Tente novamente.")
                    continue
            except ValueError:
                print("Entrada inválida! Insira números inteiros.")
                continue
        else:
            print("\nA máquina está jogando...")
            while True:
                linha_maquina = random.randint(0, 9)
                coluna_maquina = random.randint(0, 9)
                if tabuleiro_player[linha_maquina][coluna_maquina] in ['🌊', '🚢']:
                    break

            if tabuleiro_player[linha_maquina][coluna_maquina] == '🚢':
                print("💥 A máquina acertou seu navio!")
                tabuleiro_player[linha_maquina][coluna_maquina] = 'X'
                if all(cell != '🚢' for row in tabuleiro_player for cell in row):
                    print("A máquina venceu!")
                    salvar_ranking("Máquina", 1)
                    break
                # Máquina joga novamente se acertar
            else:
                print("🌊 A máquina errou!")
                tabuleiro_player[linha_maquina][coluna_maquina] = 'O'
                vez_do_jogador = True
                os.system('clear')


# Função para jogar contra a máquina
def jogar_contra_maquina():
    tabuleiro_player = criar_tabuleiro()
    tabuleiro_maquina = criar_tabuleiro()

    print("Insira seu nome:")
    nome_player = input()
    print(f"{nome_player}, posicione seus navios:")
    posicionar_navios(tabuleiro_player)

    for _ in range(4):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if tabuleiro_maquina[linha][coluna] == '🌊':
                tabuleiro_maquina[linha][coluna] = '🚢'
                break

    vez_do_jogador = True
    while True:
        if vez_do_jogador:
            print(f"\n{nome_player}, é sua vez!")
            mostrar_tabuleiro(tabuleiro_maquina)
            try:
                linha = int(input("Escolha a linha (0-9) para atacar: "))
                coluna = int(input("Escolha a coluna (0-9) para atacar: "))
                if 0 <= linha < 10 and 0 <= coluna < 10:
                    if tabuleiro_maquina[linha][coluna] == '🚢':
                        print("💥 Acertou um navio inimigo!")
                        tabuleiro_maquina[linha][coluna] = 'X'
                        if all(cell != '🚢' for row in tabuleiro_maquina for cell in row):
                            print(f"{nome_player} venceu!")
                            salvar_ranking(nome_player, 1)
                            break
                        continue  # Permanece a vez do jogador
                    elif tabuleiro_maquina[linha][coluna] == '🌊':
                        print("🌊 Errou!")
                        tabuleiro_maquina[linha][coluna] = 'O'
                        vez_do_jogador = False
                        os.system('clear')
                    else:
                        print("Você já atacou essa posição!")
                        continue
                else:
                    print("Posição fora do tabuleiro! Tente novamente.")
                    continue
            except ValueError:
                print("Entrada inválida! Insira números inteiros.")
                continue
        else:
            print("\nA máquina está jogando...")
            while True:
                linha_maquina = random.randint(0, 9)
                coluna_maquina = random.randint(0, 9)
                if tabuleiro_player[linha_maquina][coluna_maquina] in ['🌊', '🚢']:
                    break

            if tabuleiro_player[linha_maquina][coluna_maquina] == '🚢':
                print("💥 A máquina acertou seu navio!")
                tabuleiro_player[linha_maquina][coluna_maquina] = 'X'
                if all(cell != '🚢' for row in tabuleiro_player for cell in row):
                    print("A máquina venceu!")
                    salvar_ranking("Máquina", 1)
                    break
                # Máquina joga novamente se acertar
            else:
                print("🌊 A máquina errou!")
                tabuleiro_player[linha_maquina][coluna_maquina] = 'O'
                vez_do_jogador = True
                os.system('clear')


# Função para escolher o modo de jogo

def escolher_modo_jogo():
    print("Escolha o modo de jogo:")
    print("1 - Jogar contra outro jogador")
    print("2 - Jogar contra a máquina")
    print("3 - Mostrar ranking")
    escolha = input("Escolha uma opção de Jogo: ")

    if escolha == '1':
        jogar_contra_outro_player()
    elif escolha == '2':
        jogar_contra_maquina()
    elif escolha == '3':
        mostrar_ranking()
    else:
        print("Escolha inválida!")

# Chamada da função principal
escolher_modo_jogo()