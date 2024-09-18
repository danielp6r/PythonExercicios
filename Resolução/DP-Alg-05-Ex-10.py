def primo(numero):
    total = 0
    for contador in range (1 , numero + 1):
        if numero % contador == 0:
            total += 1
    if total == 2:
        return True
    else:
        return False

        
#main
numero = int(input("Digite um número inteiro positivo. "))
if primo(numero):
    print ("O número {} é primo.".format(numero))
else:
    print ("O número {} não é primo.".format(numero))