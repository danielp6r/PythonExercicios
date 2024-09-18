intervalo = int(input("Digite o intervalo de tempo expresso em número de dias, horas, minutos e segundos. DDHHMMSS: "))
dias = intervalo // 1000000
rdias = intervalo % 1000000
horas = rdias // 10000
rhoras = rdias % 10000
minutos = rhoras // 100
rminutos = rhoras % 100
segundos = rminutos 
print ("Total:",(int(dias) * 86400) + (int(horas) * 3600) + (int(minutos) * 60) + int(segundos), "segundos.")