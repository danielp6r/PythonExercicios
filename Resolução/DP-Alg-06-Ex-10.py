def stringformatada(lista):
    lista2 = ""
    for palavra in lista:
        if palavra != lista[-2] and palavra != lista[-1]:
            lista2 += palavra + ", "
        elif palavra == lista[-1]:
            lista2 += palavra 
        else:
            lista2 += palavra + " e "
    return lista2

#main
lista = input("Digite uma lista de palavras separadas por espaço: ").split()
print(stringformatada(lista))