def centraliza_string(s, larg):
    x =  int((larg - len(s))/2)
    s2 = ""
    for i in range(larg):
        s2 += "*"
    s2 += "\n"

    # acrescentar caracteres espaco antes da string original
    for i in range (x):
        s2 += " "
    # concatenar a string original com os espacos a esquerda
    s2 += s

    s2 += "\n"
    for i in range(larg):
        s2 += "*"
    return s2
    
#main
s = input("Digite uma palavra. ")
larg = int(input("Digite a largura. "))
y = centraliza_string(s, larg)
print (y)