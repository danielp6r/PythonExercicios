palavra = str(input("Digite uma palavra: "))
inverso = ""
for letra in range(len(palavra) -1, -1, -1):
    inverso += palavra[letra]
if inverso == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")