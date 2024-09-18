import random

def bingo():
    nome = "BINGO"
    cartao = dict()
    for i,letra in enumerate(nome):
        lista = list(range(i*15 +1, i*15 + 16))
        numeros = random.sample(lista,5)
        numeros.sort()
        cartao[letra] = numeros
    return cartao


def mostra_bingo(cartao):
    numeros_colunas = list(cartao.values())
    numeros_linhas = list(zip(*numeros_colunas))
    print('%2s\t%2s\t%2s\t%2s\t%2s\t'% tuple('BINGO'))
    for linha in numeros_linhas:
        print('%2s\t%s\t%s\t%s\t%s\t'% linha)


#main
cartao = bingo()
mostra_bingo(cartao)