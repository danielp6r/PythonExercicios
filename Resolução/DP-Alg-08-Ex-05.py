def soma(n):
    n = input ("Digite um número (Enter para): ")
    if n == "":
        return 0.0
    else:
        return float(n) + soma(n)


print ("A soma dos números é: ", soma(0.0))