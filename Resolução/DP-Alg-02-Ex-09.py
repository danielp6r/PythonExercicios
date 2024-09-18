data = int(input("Digite a data no formato DDMMAA. "))
dia = data // 10000
rdia = data % 10000
mes = rdia // 100
rmes = rdia % 100
ano = rmes
print (ano, mes, dia, sep="")