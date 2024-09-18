mes = str(input("Digite um mês do ano. (Por extenso.) "))
if mes == "Janeiro" or mes == "janeiro" or mes == "Março" or mes == "março" or mes == "Maio" or mes == "maio" or mes == "Julho" or mes == "julho" or mes == "Agosto" or mes == "agosto" or mes == "Outubro" or mes == "outubro" or mes == "Dezembro" or mes == "dezembro":
    print("O mês de", mes, "tem 31 dias. ")
elif mes == "Fevereiro" or mes == "fevereiro":
    print("O mês de", mes, "tem 28 dias.(29 dias nos anos bissextos.)")
elif mes == "Abril" or mes == "abril" or mes == "Junho" or mes == "junho" or mes == "Setembro" or mes == "setembro" or mes == "Novembro" or mes == "novembro":
    print("O mês de", mes, "tem 30 dias.")
else:
    print("Erro. Mês inválido.")