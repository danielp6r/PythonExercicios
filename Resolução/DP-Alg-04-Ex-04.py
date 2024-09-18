import math
xx1 = 0
yy1 = 0
p = 0
x1 = 0
y1 = 0
xn = 0
yn = 0
x1 = float(input("Digite a coordenada x do primeiro vértice: "))
y1 = float(input("Digite a coordenada y do primeiro vértice: "))
xx1 = float(x1)
yy1 = float(y1)
while xn != "":
    xn = input("Digite a coordenada x do prox. vértice ou deixe em branco para sair(Enter): ")
    if xn != "":
        yn = float(input("Digite a coordenada y do prox. vértice: "))
        x2 = float(xn)
        y2 = float(yn)
        p = p + math.sqrt (((y2 - yy1)**2) + ((x2 - xx1)**2))
        xx1 = float(x2)
        yy1 = float(y2)
else: p = p + math.sqrt (((y2 - y1)**2) + ((x2 - x1)**2))
print("O perímetro do polígono é: ", p)