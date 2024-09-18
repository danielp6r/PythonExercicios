def diasnomes(mes, ano):
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return 31
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            return 30
        elif mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                return 29
            else:
                return 28

#main
mes = int(input("Digite o mês (de 1 a 12): "))
ano = int(input("Digite o ano: "))
x = diasnomes(mes, ano)
print("O mês tem", x, "dias")