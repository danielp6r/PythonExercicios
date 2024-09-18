vlr_in_dep = float (input("Digite o valor inicial depositado na conta. "))
ano1 = 1
ano2 = 2
ano3 = 3 
juros = 12/100
vlr_1ano = vlr_in_dep * (1 + juros) ** ano1 
vlr_2ano = vlr_in_dep * (1 + juros) ** ano2
vlr_3ano = vlr_in_dep * (1 + juros) ** ano3
print (f'O valor final depois de 1 ano é de R${vlr_1ano:,.2f}.')
print (f'O valor final depois de 2 anos é de R${vlr_2ano:,.2f}.')
print (f'O valor final depois de 3 anos é de R${vlr_3ano:,.2f}.')