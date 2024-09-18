valor1 = 4.95
for i in range (0,5):
    print (f'Valor: R${valor1:,.2f}.' , end=" ")
    desconto = valor1 * 0.6
    print (f'Desconto: R${desconto:,.2f}.' , end=" ")
    valor2 = valor1 * 0.4
    print (f'Valor final: R${valor2:,.2f}.')
    valor1 += 5