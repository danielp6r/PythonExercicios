segundos = int(input("Digite a quantidade de segundos. "))
dias = segundos // 86400
segundos_rest = segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60
print("Tempo convertido: {:d} dias {:02d} horas {:02d} minutos e {:02d} segundos".format(dias, horas, minutos, segundos_rest))