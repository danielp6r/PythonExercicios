palavra = input("Digite uma palavra binária de 8 bits: ")

if len(palavra) != 8:
    print("Erro. Número de bits inválido!")
n = 0
for bit in palavra:
    if bit != "0" and bit != "1":
        print("Erro. Palavra inválida!")
    elif bit == "1":
        n += 1
if n%2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"
print("Palavra:", palavra, "Paridade:", paridade)