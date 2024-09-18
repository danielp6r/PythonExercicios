def somentepalavras(s):
    import string
    s2 = "".join([i for i in s if i not in string.punctuation])
    lista = s2.split()
    return lista

   
#main
s = input("Digite uma frase: ")
lista = somentepalavras(s)
print(lista)