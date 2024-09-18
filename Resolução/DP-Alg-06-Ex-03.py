def copiadalista(lista, n):
    lista2 = lista[n:-n]
    return lista2


#main
n = 2
lista = input("Digite os números da lista: (Separados por espaço) ").split()
lista = [int(x) for x in lista]
if len(lista) <= 4:
    print("Lista inválida.")
else:
    print("Lista Modificada: ", copiadalista(lista, n))
    print("Lista Original: ", lista)