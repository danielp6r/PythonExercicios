def DecBinRecursivo(n):
    if n < 0:
        return "Não é possível converter números negativos"
    elif n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return DecBinRecursivo(n // 2) + str(n % 2)


#main
x = int(input("Digite um número inteiro: "))
q = DecBinRecursivo(x)
print("O número", x, "em binário é:", q)
print (type(q))