def parabase10(string, base):
    if base == 2:
        return int(string, 2)
    elif base == 16:
        return int(string, 16)

def parastring(numbase10, base):
    if base == 2:
        return bin(numbase10)
    elif base == 16:
        return hex(numbase10)


#main
print (""" Digite:
(1) para converter para decimal;
(2) para converter de decimal para outras bases""")
opção = int(input("Digite a opção desejada: "))
if opção == 1:
    string = input("Digite um número: ")
    base = int(input("Digite a base atual: "))
    if base == 2 or base == 16:
        x = parabase10(string, base)
        if base == 2:
            print("O número binário {} corresponde ao número decimal {}".format(string, x))
        elif base == 16:
            print("O número hexadecimal {} corresponde ao número decimal {}".format(string, x))
elif opção == 2:
    numbase10 = int(input("Digite um número inteiro: "))
    print (""" Escolha uma das opções abaixo:
    (1) para converter para binário;
    (2) para converter para hexadecimal""")
    opção = int(input("Digite a opção desejada: "))
    if opção == 1:
        x = parastring(numbase10, 2)
        print("O número decimal {} corresponde ao número binário {}".format(numbase10, x[2:]))
    elif opção == 2:
        x = parastring(numbase10, 16)
        print("O número decimal {} corresponde ao número hexadecimal {}".format(numbase10, x[2:]))
    else:
        print("Opção inválida")