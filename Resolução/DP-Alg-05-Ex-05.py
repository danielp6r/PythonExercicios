def n(num):
    cont = ("Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto", "Sexto", "Sétimo", "Oitavo", "Nono", "Décimo", "Décimo primeiro", "Décimo segundo")
    while num < 13 and num > 0:
        return cont[num-1]
    else:
        return " "

#main
for i in range(1, 13):
    print(i,n(i))