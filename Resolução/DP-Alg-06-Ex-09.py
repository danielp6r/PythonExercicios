abaixo = list()
medios = list()
acima = list()
num = 1
numeros = [num]
while num != 0:
    num = str(input("Digite um número (Enter para parar): "))
    if num == "":
        break
    else:
        num = int(num)
        numeros.append(num)
numeros = numeros[1:]
média = sum(numeros) / len(numeros)
print(f"A média dos números é {média}")
for numero in numeros:
    if numero < média:
        abaixo.append(numero)
    elif numero > média:
        acima.append(numero)
    else:
        medios.append(numero)
print(f"Os números abaixo da média são: {abaixo}")
print(f"Os números na média são: {medios}")
print(f"Os números acima da média são: {acima}")