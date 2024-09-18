numero = int(input("Digite um número inteiro: "))
result = str("")
q = numero
while q > 0:
    r = q % 2
    q = q // 2
    result = str(r) + result
print(result)