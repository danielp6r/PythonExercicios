def datamagica(dia, mes, ano):
    decada = ano[2:]
    dia = int(dia)
    mes = int(mes)
    decada = int(decada)
    if dia * mes == decada:
        return True
    else:
        return False


#main
for ano in range(1900, 2001):
    for mes in range(1, 13):
        for dia in range(1, 32):
            ano = str(ano)
            mes = str(mes)
            dia = str(dia)
            x = datamagica(dia, mes, ano)
            if x == True:
                print("O dia", dia, "do mês", mes, "do ano", ano, "é uma data mágica. ")    