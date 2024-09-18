alfabeto = "abcdefghijklmnopqrstuvwxyz"
list(alfabeto)

mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave: "))
cifra = ""

for letra in mensagem:
    indice = ord(letra)-19
    cifra+= alfabeto[(indice+chave) %len(alfabeto)] if letra in alfabeto else letra

print(cifra)