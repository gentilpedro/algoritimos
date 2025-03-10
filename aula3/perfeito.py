num = int(input("Número: "))

print(f"Divisores do {num}: ", end="")
soma = 0

for i in range(1, int(num/2)+1):
  if num % i == 0:
    print(f"{i}, ", end="")
    soma = soma + i

print(f"\nSoma: {soma}")

if soma == num:
  print(f"Portanto, {num} é um número Perfeito")
else:
  print(f"Ah... {num} Não é um número perfeito")