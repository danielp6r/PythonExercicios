import random
numerossorteados = list()
while len(numerossorteados) < 6:
    x = random.randint(1,60)
    if x not in numerossorteados:
        numerossorteados.append(x)
numerossorteados.sort()
print("Números sorteados:",numerossorteados)