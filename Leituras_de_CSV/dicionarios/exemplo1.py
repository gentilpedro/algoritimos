# Principal aplicação com uso de dicionários: Lista de Dicionários
clientes = [
  {"nome": "Pedro Santos", "idade": 30},
  {"nome": "Martina da Costa", "idade": 21},
  {"nome": "André Pereira", "idade": 34},
  {"nome": "Bianca de Mattos", "idade": 19},
  {"nome": "Tiago Gonçalves", "idade": 24},
]

# pode-se acrescentar itens na lista
clientes.append({"nome": "Cláudia Silva", "idade": 38})

# exibir um elemento da lista
print(clientes[0])

# e, exibir apenas um atributo (chave) deste elemento
print(clientes[0]['nome'])

print("-"*30)

# formas de percorrer a lista
for cliente in clientes:
  print(cliente['nome'])

print("="*30)

# formas de percorrer a lista
for contador, cliente in enumerate(clientes, start=1):
  print(f"{contador}º Cliente: {cliente['nome']}")

# -------------------- Classificar / ordenar a lista
# lambda: forma de declarar funções anônimas com o Python
# Equivale as Arrow Functions () => {} do JavaScript
clientes2 = sorted(clientes, key=lambda cliente: cliente['nome'])

print("*"*30)

# mostra a lista ordenada por nome
for contador, cliente in enumerate(clientes2, start=1):
  print(f"{contador}º Cliente: {cliente['nome']}")

# ----------- Ordenar e exibir a lista em ordem decrescente de idade
clientes3 = sorted(clientes, key=lambda cliente: cliente['idade'], 
                   reverse=True)

print("*"*30)

# mostra a lista ordenada por idade
for contador, cliente in enumerate(clientes3, start=1):
  print(f"{contador}º Cliente: {cliente['nome']} - {cliente['idade']} anos")

# ---------------- Filtros na lista
print("+"*30)

for contador, cliente in enumerate(clientes, start=1):
  if cliente['idade'] >= 30:
    print(f"{contador}º Cliente: {cliente['nome']} - {cliente['idade']} anos")

print("*"*30)

# --- Filtros com List Comprehensions
clientes4 = [cliente for cliente in clientes if cliente['idade'] < 30]
# clientes4 = [x for x in clientes if x['idade'] < 30]

for contador, cliente in enumerate(clientes4, start=1):
  print(f"{contador}º Cliente: {cliente['nome']} - {cliente['idade']} anos")

num = len(clientes4)
print(f"{num} clientes menores que 30 anos")