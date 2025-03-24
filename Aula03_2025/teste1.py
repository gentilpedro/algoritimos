palavra =input("Qual a palavra: ")

letra = input("Letra: ").upper()

if palavra.upper().find(letra) >=0 :
    print("ok! Letra consta na palavra")
else:
    print("Erro... Letra não consta")