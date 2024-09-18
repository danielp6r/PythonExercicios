def DecBinIterativo(q):
    binario = ""
    while q != 0:
        binario = str(q % 2) + binario
        q = q // 2
    return binario


#main
x = int(input("Digite um número inteiro: "))
q = DecBinIterativo(x)
print("O número {} em binário é {}".format(x, q))
print (type(q))