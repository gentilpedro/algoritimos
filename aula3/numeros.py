print("Informe os números ou 0 para sair")

quant = 0
soma = 0
maior = 0

while True:
  num = int(input("Número: "))
  if num == 0:
    break
  quant = quant + 1
  soma = soma + num
  if num > maior:
    maior = num

print("-"*30)  
print(f"Quantidade de Números Digitados: {quant}")
print(f"Soma dos Números: {soma}")
print(f"Maior Número: {maior}")