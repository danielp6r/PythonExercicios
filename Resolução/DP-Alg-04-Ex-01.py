soma = 0
n = 0

x = 1
while x != 0:
    x = float(input("Digite um número (0 para parar): "))
    if x == 0 and n == 0:
        print("Erro. Nenhum número foi digitado")
        break
    elif x != 0:
        soma += x
        n += 1
else:
    media = soma / n
    print ("A média dos números é: ", media)