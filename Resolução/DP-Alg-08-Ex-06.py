def MDC(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return MDC(b, c)
       

#main
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print ("O MDC é: ", MDC(a, b))