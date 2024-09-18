palavras = list()
while True:
    palavra = str(input("Digite uma palavra: "))
    if palavra == "":
        break
    if palavra in palavras:
        print("Palavra já existe.")
    else:
        palavras.append(palavra)
for palavra in palavras:
    print(palavra)