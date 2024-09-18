binario = str(input("Digite um número binário: "))
decimal = 0
for i in range(len(binario)):
    if binario[i] == "1":
        decimal += 2 ** (len(binario) - i - 1)
print(decimal)