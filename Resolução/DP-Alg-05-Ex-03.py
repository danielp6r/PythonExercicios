def qtd(qtditens):
    if qtditens == 1:
        return 10.95
    elif qtditens > 1:
        return 10.95 + (qtditens - 1) * 2.95
    else:
        print ("Quantidade inválida")

# main
qtditens = int(input("Digite a quantidade de itens: "))
x = qtd(qtditens)
print(f"O custo de envio é: R${x:,.2f}")