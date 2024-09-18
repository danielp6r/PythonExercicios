def buscaReversa(dicionario, valor):
    x = []
    if valor in dicionario:
        return dicionario[valor]
    else:
        return []


#main
dicionario = {1: ("a", "b", "x", "y"), 2: ("c", "d", "z"), 3: ("e", "f"), 4: "g", 5: "h"}
valor = int(input("Digite um valor: "))
print(buscaReversa(dicionario, valor))