def x(c1, c2, c3):
    t = 0
    if (c1 >= c2 + c3) or (c2 >= c1 + c3) or (c3 >= c1 + c2):
        t = 0
    else:
         t = 1
    return t

#main
c1 = int(input("Digite o valor de canudo 1: "))
c2 = int(input("Digite o valor de canudo 2: "))
c3 = int(input("Digite o valor de canudo 3: "))
y = x(c1, c2, c3)
if y == 1:
    print ("Triângulo Válido. ")
else: 
    print ("Triangulo Inválido. ")