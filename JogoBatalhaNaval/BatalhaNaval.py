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
            linha = int(input("Escolha a linha (0-10): "))
            coluna = int(input("Escolha a coluna (0-10): "))
            if tabuleiro[linha][coluna] == '🌊':  # Verifica se já há navio
                tabuleiro[linha][coluna] = '🚢'  # Marca o navio
                break
            else:
                print("Essa posição já está ocupada!")

# Função para salvar o ranking no arquivo JSON
def salvar_ranking(nome, vitorias):
    # Verifica se o arquivo de ranking já existe, senão cria um novo
    if os.path.exists('ranking.json'):
        with open('ranking.json', 'r') as f:
            ranking = json.load(f)
    else:
        ranking = []

    # Adiciona o novo jogador ou atualiza as vitórias
    encontrado = False
    for jogador in ranking:
        if jogador['nome'] == nome:
            jogador['vitorias'] = vitorias
            encontrado = True
            break

    if not encontrado:
        ranking.append({'nome': nome, 'vitorias': vitorias})

    # Ordena o ranking por vitórias (do maior para o menor)
    ranking = sorted(ranking, key=lambda x: x['vitorias'], reverse=True)

    # Salva o ranking atualizado no arquivo
    with open('ranking.json', 'w') as f:
        json.dump(ranking, f, indent=4)

# Função para carregar o ranking do arquivo JSON
def carregar_ranking():
    if os.path.exists('ranking.json'):
        with open('ranking.json', 'r') as f:
            ranking = json.load(f)
        return ranking
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
def jogar_contra_outro_player():
    tabuleiro_player1 = criar_tabuleiro()
    tabuleiro_player2 = criar_tabuleiro()

    print("Jogador 1, insira seu nome:")
    nome_player1 = input()
    print(f"{nome_player1}, posicione seus navios:")
    posicionar_navios(tabuleiro_player1)
    print("Tabuleiro de Jogador 1:")
    mostrar_tabuleiro(tabuleiro_player1)

    print("\nAgora, Jogador 2, insira seu nome:")
    nome_player2 = input()
    print(f"{nome_player2}, posicione seus navios:")
    posicionar_navios(tabuleiro_player2)
    print("Tabuleiro de Jogador 2:")
    mostrar_tabuleiro(tabuleiro_player2)

    # Começa a batalha
    jogador_atual = nome_player1
    tabuleiro_atual = tabuleiro_player1
    tabuleiro_oponente = tabuleiro_player2

    while True:
        print(f"\n{jogador_atual}, é sua vez!")
        mostrar_tabuleiro(tabuleiro_atual)

        linha = int(input("Escolha a linha (0-4) para atacar: "))
        coluna = int(input("Escolha a coluna (0-4) para atacar: "))

        if tabuleiro_oponente[linha][coluna] == 'N':
            print("💥 Acertou um navio inimigo!")
            tabuleiro_oponente[linha][coluna] = 'X'  # Marca o navio atingido
            if all(cell != 'N' for row in tabuleiro_oponente for cell in row):
                print(f"{jogador_atual} venceu!")
                if jogador_atual == nome_player1:
                    salvar_ranking(nome_player1, 1)
                    salvar_ranking(nome_player2, 0)
                else:
                    salvar_ranking(nome_player2, 1)
                    salvar_ranking(nome_player1, 0)
                break
        else:
            print("🌊 Errou!")
            tabuleiro_oponente[linha][coluna] = 'O'  # Marca o erro

        # Troca de jogador
        if jogador_atual == nome_player1:
            jogador_atual = nome_player2
            tabuleiro_atual = tabuleiro_player2
            tabuleiro_oponente = tabuleiro_player1
        else:
            jogador_atual = nome_player1
            tabuleiro_atual = tabuleiro_player1
            tabuleiro_oponente = tabuleiro_player2

# Função para jogar contra a máquina
def jogar_contra_maquina():
    tabuleiro_player = criar_tabuleiro()
    tabuleiro_maquina = criar_tabuleiro()

    print("Insira seu nome:")
    nome_player = input()
    print(f"{nome_player}, posicione seus navios:")
    posicionar_navios(tabuleiro_player)
    print("Tabuleiro do jogador:")
    mostrar_tabuleiro(tabuleiro_player)

    # Posicionando os navios da máquina aleatoriamente
    for _ in range(3):
        while True:
            linha = random.randint(0, 4)
            coluna = random.randint(0, 4)
            if tabuleiro_maquina[linha][coluna] == '~':
                tabuleiro_maquina[linha][coluna] = 'N'
                break

    # Começa a batalha
    tabuleiro_atual = tabuleiro_player
    tabuleiro_oponente = tabuleiro_maquina

    while True:
        print(f"\n{nome_player}, é sua vez!")
        mostrar_tabuleiro(tabuleiro_atual)

        linha = int(input("Escolha a linha (0-4) para atacar: "))
        coluna = int(input("Escolha a coluna (0-4) para atacar: "))

        if tabuleiro_oponente[linha][coluna] == 'N':
            print("💥 Acertou um navio inimigo!")
            tabuleiro_oponente[linha][coluna] = 'X'
            if all(cell != 'N' for row in tabuleiro_oponente for cell in row):
                print(f"{nome_player} venceu!")
                salvar_ranking(nome_player, 1)
                break
        else:
            print("🌊 Errou!")
            tabuleiro_oponente[linha][coluna] = 'O'

        # A vez da máquina
        print("\nA máquina está jogando...")
        linha_maquina = random.randint(0, 4)
        coluna_maquina = random.randint(0, 4)
        print(f"A máquina ataca: {linha_maquina}, {coluna_maquina}")

        if tabuleiro_atual[linha_maquina][coluna_maquina] == 'N':
            print("💥 A máquina acertou seu navio!")
            tabuleiro_atual[linha_maquina][coluna_maquina] = 'X'
            if all(cell != 'N' for row in tabuleiro_atual for cell in row):
                print("A máquina venceu!")
                salvar_ranking("Máquina", 1)
                break
        else:
            print("🌊 A máquina errou!")
            tabuleiro_atual[linha_maquina][coluna_maquina] = 'O'

# Função para escolher o modo de jogo
def escolher_modo_jogo():
    print("Escolha o modo de jogo:")
    print("1 - Jogar contra outro jogador")
    print("2 - Jogar contra a máquina")
    print("3 - Mostrar ranking")
    escolha = input()

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
