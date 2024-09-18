idade = 0
ate2 = 0
de3a12 = 0
mais65 = 0
ingressopadrão = 0
while True:
    idade = (input("Digite a idade de um membro do grupo (Enter para fim): "))
    if idade == "":
        break
    elif int(idade) <= 2:
        ate2 += 1
    elif int(idade) <= 12:
        de3a12 += 1
    elif int(idade) >= 65:
        mais65 += 1
    else:
        ingressopadrão += 1
valortotal = (ate2 * 0) + (de3a12 * 14) + (mais65 * 18) + (ingressopadrão * 23)
print (f"Valor total: R$ {valortotal:,.2f}")

