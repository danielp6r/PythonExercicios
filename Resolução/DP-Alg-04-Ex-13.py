fator = 2
n = int(input("Digite um número inteiro maior ou igual a 2: "))
if n < 2:
    print("Erro, número inválido!")
else:
    pass
while fator <= n:
    if n % fator == 0:
        n = n / fator
    else:
        fator += 1