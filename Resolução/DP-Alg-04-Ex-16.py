import random
contatodos = 0
for i in range(10):
    print("Rodada", i+1, end=" ")
    contador = 0
    cara = 0
    coroa = 0
    while cara < 3 and coroa < 3:
        lançar = random.randint(0,1)
        if lançar == 0:
            print ("A", end=" ")
            cara += 1
            contador += 1
            coroa = 0
            contatodos += 1
        elif lançar == 1:
            print ("O", end=" ")
            coroa += 1
            contador += 1
            cara = 0
            contatodos += 1
    print("({:d} sorteios)".format(contador))
print ("Na média foram necessários ", contatodos/10,  "sorteios.")

