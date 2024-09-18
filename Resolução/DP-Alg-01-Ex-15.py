from math import pi, tan


l = float(input("Digite o comprimento de um lado do polígono. "))
n = float(input("Digite o numero de lados que o polígono possúi. "))
area = n * (l**2) / (4*tan(pi/n))
print ("A área do polígono regular é:",area, ".")