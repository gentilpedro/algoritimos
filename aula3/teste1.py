palavra = "computador"

letra = input("Letra: ")

if palavra.find(letra) >= 0:
  print("Letra consta na palavra")
else:
  print("Não consta")