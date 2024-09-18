def precedencia(operador):
    if operador == "+" or operador == "-":
        return 1
    elif operador == "*" or operador == "/":
        return 2
    elif operador == '^':
        return 3
    else:
        return 0

#main
operador = input("Digite o operador: ")
x = precedencia(operador)
if x != 1 and x != 2 and x != 3:
    print ("Erro. Operador invalido")
else:
    print ("Operador: ",operador)
    print ("Procedência: ",x)