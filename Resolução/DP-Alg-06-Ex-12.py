def issorted(lista):
    if lista == sorted(lista) or lista == sorted(lista, reverse=True):
        return True
    else:
        return False


#main
lista = input("Digite uma lista de palavras separadas por espaço: ").split()
print (issorted(lista))
if len(lista) == 1:
    print("A lista contém apenas um número e está em ordem.")
elif len(lista) == 0:
    print("A lista é vazia e está em ordem.")