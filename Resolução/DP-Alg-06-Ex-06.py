def divisores(n):
    divisores = list()
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores


#main
numero = int(input("Digite um número inteiro positivo. "))
x = divisores(numero)
print ("Número = ", numero)
print ("Divisores = ", x)