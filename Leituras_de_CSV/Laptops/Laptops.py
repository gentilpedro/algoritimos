import csv
from collections import Counter

laptops = []

with open("laptop_prices.csv", mode="r") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        laptops.append(linha)


def titulo(texto):
    print()
    print(texto)
    print("-" * 40)


def top10_marcas():
    # Top 10 marcas com maior número de modelos
    titulo("Top 10 Marcas com maior numero de modelos")
    
    # Contar o número de modelos por marca
    index = Counter(laptop["Company"] for laptop in laptops)
    
    # Obter as 10 marcas com o maior número de modelos
    top10marcas = index.most_common(10)
    
    print("Marca....................... Nº Modelos")
    print("---------------------------------------")
    
    for i, (marca, quantidade) in enumerate(top10marcas, start=1):
        print(f"{i:2d} {marca:20s} {quantidade:10d}")

def top20_caros():
    # Top 20 laptopss mais caros
    titulo("Top 20 Mais Caros")
    
    # Ordena os laptops por preço em ordem decrescente
    notes_caros = sorted(laptops, key=lambda laptop:
        
    float(laptop['Price_euros']), reverse=True)
    
    print("Marca.................. Modelo...................... Preço (€)")
    print("--------------------------------------------------------------")

    for i, laptop in enumerate(notes_caros[:20], start=1):
        print(f"{i:2d} {laptop['Company']:20s} {laptop['Product']:25s} {float(laptop['Price_euros']):10.2f}")

def compara_marcas():
    # Aqui começo exibindo o titulo da função e insiro as marcas de notes
    titulo("Comparar Média de Preços de 2 Marcas")
    marca1 = input("1ª Marca: ").upper()
    marca2 = input("2ª Marca: ").upper()
    
    #Aqui inicializo os totalizadores e contadores
    total1 = 0
    total2 = 0
    contador1 = 0
    contador2 = 0
    modelos1 = []
    modelos2 = []
    
    for laptop in laptops:
        if laptop['Company'].upper() == marca1:
            #Nessa parte eu adiciono o preço de cada modelo da marca 1 e vou
            #adicionando no contador o numero de marcas para fazer a media depois
            total1 += float(laptop['Price_euros'])
            contador1 += 1
            modelos1.append(laptop['Product'])
        elif laptop['Company'].upper() == marca2:
    #Nessa parte eu adiciono o preço de cada modelo da marca 2 e vou
    #adicionando no contador o numero de marcas para fazer a media depois
                total2 += float(laptop['Price_euros'])
                contador2 += 1
                modelos2.append(laptop['Product'])
    
    # Aqui eu faço os calculos das médias com os dados dos contadores e dos
    #totalizadores que adiquiri no loop anterior
    
    media1 = total1 / contador1 if contador1 > 0 else 0
    media2 = total2 / contador2 if contador2 > 0 else 0
    
    # Essa parte é para printar no sistema a Marca em seguida a lista de
    #modelo e no final a media de preços dos notes que tem aquela marca
    
    print(f"\nModelos da marca {marca1}:")
    
    for modelo in modelos1:
        print(f"- {modelo}")
        print(f"Média de preços para {marca1}: {media1:10.2f} €")
        print(f"\nModelos da marca {marca2}:")
    
    for modelo in modelos2:
        print(f"- {modelo}")
        print(f"Média de preços para {marca2}: {media2:10.2f} €")
        
def pesquisa_preço():
    titulo("Pesquisa de Laptops por Intervalo de Preço")
    # Vamos ler os preços nesse input
    #botei esse bloco try pra eu me assegurar que os valores inseridos serão
    #numericos
    try:
        preco_min = float(input("Digite o preço mínimo (€) ex 0000.00: "))
        preco_max = float(input("Digite o preço máximo (€) ex 0000.00: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return        

    #    Aqui eu filtro os laptops dentro do intervalo de preço
laptops_encontrados = [
    
laptop for laptop in laptops

if preco_min <= float(laptop['Price_euros']) <= preco_max
    ]
    # Aqui eu faço a verificação para que se foram encontrados laptops
    #mostrar os dados pedidos no exercicio se nao exibir uma mesnsagem de nao
    #encontrado
if laptops_encontrados:
    
    print(f"\Laptops encontrados entre {preco_min:.2f} € e{preco_max:.2f} €:")
    print("Marca............... Modelo................... Preço (€)")
    print("----------------------------------------------------------")
    
for laptop in laptops_encontrados:  
    print(f"{laptop['Company']:20s} {laptop['Product']:25s} {laptop['Price_euros']:10} €")
else:
    print("Nenhum laptops encontrado dentro do intervalo de preço especificado.")
  
        
        
# -------------------------------- Programa Principal
while True:
    titulo("Dados de Laptops")
    print("1. Top 10 Marcas")
    print("2. Top 20 Mais Caros")
    print("3. Comparar duas Marcas")
    print("4. Pesquisar por faixa de Preço")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top10_marcas()
    elif opcao == 2:
        top20_caros()
    elif opcao == 3:
        compara_marcas()
    elif opcao == 4:
        pesquisa_preço()
    else:
        break
