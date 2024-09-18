l1 = float(input("Digite o comprimento do lado 1 de um triângulo."))
l2 = float(input("Digite o comprimento do lado 2 de um triângulo."))
l3 = float(input("Digite o comprimento do lado 3 de um triângulo."))
if l1 == l2 and l1 == l3:
    print ("O triângulo é equiláero.")
elif (l1 == l2 and l1 != l3) or (l1 !=l2 and l1 == l3):
    print ("O triângulo é isósceles. ")
else:
    print ("O triângulo é escaleno. ")