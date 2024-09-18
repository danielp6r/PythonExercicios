def countRange(lista, valormin, valormax):
    count = 0
    for i in lista:
        if i >= valormin and i < valormax:
            count += 1
    return count


#main
lista = range (-1000, 1000)
valormin = -500
valormax = 500
print(countRange(lista, valormin, valormax))