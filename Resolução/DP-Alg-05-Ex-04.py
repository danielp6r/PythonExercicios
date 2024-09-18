def media(a, b, c):
    return (a + b + c) / 3

#main
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
x = media(a, b, c)
print(f"A média é: {x:.2f}")