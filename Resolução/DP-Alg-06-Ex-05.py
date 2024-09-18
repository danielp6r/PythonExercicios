numeros = list()
negativos = list()
neutros = list()
positivos = list()
while True:
    numero = str(input("Digite um número (Enter para parar): "))
    if numero == "":
        break
    else:
        numero = int(numero)
        if numero < 0:
            negativos.append(numero)
        elif numero == 0:
            neutros.append(numero)
        else:
            positivos.append(numero)
for numero in negativos:
    print(numero)
for numero in neutros:
    print(numero)
for numero in positivos:
    print(numero)