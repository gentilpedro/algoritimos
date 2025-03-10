pessoas = int(input("Nº Pessoas: "))
peixes = int(input("Nº Peixes: "))

total = pessoas * 20

if peixes > pessoas:
  extras = peixes - pessoas
  total = total + (extras * 12)

print(f"Pagar R$: {total:.2f}")