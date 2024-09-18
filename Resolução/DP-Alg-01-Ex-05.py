vasilhame_menor = 10
vasilhame_maior = 25
qtd_menor = float (input("Digite a quantidade de vasilhames com 1l ou menos. " ))
qtd_maior = float (input("Digite a quantidade de vasilhames com mais de 1l. " ))
total = ((qtd_menor * vasilhame_menor) + (qtd_maior * vasilhame_maior)) / 100
print (f'O valor de retorno é de R${total:,.2f}.')