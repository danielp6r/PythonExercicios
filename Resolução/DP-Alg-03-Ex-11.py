a = int(input("Digite o valor de a: "))
if a != 0:
    pass
else:
    print("O valor de a não pode ser zero")
    exit()
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = (b**2 - 4*a*c)
x1 = (-b + d**0.5)/(2*a)
x2 = (-b - d**0.5)/(2*a)
if d < 0:
    print("Não existe raiz real")
elif d == 0:
    print("Existe uma raiz real")
    print("x=", x1)
else:
    print("Existe duas raizes reais")
    print ("x1 =", x1)
    print ("x2 =", x2)