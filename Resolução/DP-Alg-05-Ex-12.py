def senhavalida(senha):
    a, b, c = 0, 0, 0
    if len(senha) < 8:
        return False
    for i in senha:
        if (i.islower()):
            a += 1
        if (i.isupper()):
            b += 1
        if (i.isdigit()):
            c += 1
    if (a == 0 or b == 0 or c == 0):
        return False
    else:
        return True
            

#main
senha = input("Digite uma senha: ")
if senhavalida(senha):
    print("A senha é válida")
else:
    print("A senha é inválida")