anos = int(input("Digite a quantidade de anos cronológicos. "))
if anos < 0:
    print("Erro. Você digitou um número negativo. ")
elif anos <=2:
    print (anos * 10.5, "Anos canínos. ")
else: print (21 + (anos - 2) * 4.5, "Anos canínos. ")