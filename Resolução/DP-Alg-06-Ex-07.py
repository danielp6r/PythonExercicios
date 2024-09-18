def divisores(n):
    divisores = list()
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def numeroperfeito(n):
    x = divisores(n)
    soma = sum(x)
    soma = soma - n
    if soma == n:
        return True
    else:
        return False


#main
#Código ruim == demora pra calcular :/
for i in range(1, 10000):
    if numeroperfeito(i):
        print(i)
    else:
        continue