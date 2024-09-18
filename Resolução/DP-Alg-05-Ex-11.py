def senhaaleatória():
    import string
    import random
    escolhas_possiveis = string.ascii_letters + string.digits + string.punctuation
    resultado = ""
    len = random.randint(7, 10)
    for i in range(len):
        resultado += random.choice(escolhas_possiveis)
    return resultado


#main
senha = senhaaleatória()
print("A senha gerada foi: {}".format(senha))