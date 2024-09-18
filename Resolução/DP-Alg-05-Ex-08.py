def maiusculo(s):
    s2 = s.capitalize()
    c = ""
    upper = True
    for letra in s2:
        if letra == "?":
            c += letra
            upper = True
        elif letra != "?" and letra != ' ' and upper:
            c += letra.upper()
            upper = False
        elif letra == ".":
            c += letra
            upper = True
        elif letra != "." and letra != ' ' and upper:
            c += letra.upper()
            upper = False
        elif letra == "!":
            c += letra
            upper = True
        elif letra != "!" and letra != ' ' and upper:
            c += letra.upper()
            upper = False
        else:
            c += letra
    return c


#main
s = input("Digite uma frase: ")
print(maiusculo(s))