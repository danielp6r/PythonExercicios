num = 1
numeros = [num]
while num != 0:
    num = int(input("Digite um número (0 para parar): "))
    if num != 0:
        numeros.append(num)
numeros = numeros[1:]
numeros.sort()
print (numeros)