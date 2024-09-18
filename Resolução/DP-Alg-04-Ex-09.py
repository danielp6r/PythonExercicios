x = int(input("Número: "))
r = x/2
while r * r > 0.1 ** -12:
    r = (r + (r / 2)) / 2
print("Raíz:", r)