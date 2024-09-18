from math import radians, acos, cos, sin


print("Digite a latitude e longitude de dois pontos na terra em graus:")
t1 = float(input(" Latitude 1: "))
g1 = float(input(" Longitude 1: "))
t2 = float(input(" Latitude 2: "))
g2 = float(input(" Longitude 2: "))
t1 = radians(t1)
g1 = radians(g1)
t2 = radians(t2)
g2 = radians(g2)
distancia = 6371.01 * acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print("A distância é: ",distancia,"Km. ")