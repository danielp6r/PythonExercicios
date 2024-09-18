peso_bg = 75 
peso_qq = 112
qtd_bg = int (input("Digite a quantidade de bugigangas. " ))
qtd_qq = int (input("Digite a quantidade de quinquilharias. " ))
peso_gramas = ((qtd_bg * peso_bg) + (qtd_qq * peso_qq))
peso_quilos = (peso_gramas)/1000
print (f'O peso total do pedido é de {peso_quilos:,.3f}kg.')