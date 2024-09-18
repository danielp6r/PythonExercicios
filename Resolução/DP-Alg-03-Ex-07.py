britadeira = 130
cortador = 106
despertador = 70
sala = 40
db = int(input("Digite um nível de volume em decibéis. "))
if db == britadeira:
    print ("O valor é equivalente aos decibéis da britadeira. ")
elif db == cortador:
    print ("O valor é equivalente aos decibéis do cortador de grama. ")
elif db == despertador:
    print ("O valor é equivalente aos decibéis do despertador. ")
elif db == sala:
    print ("O valor é equivalente aos decibéis de uma sala silenciosa. ")
elif db < britadeira and db > cortador:
    print ("O valor está entre os decibéis da britadeira e do cortador de grama. ")
elif db < cortador and db > despertador:
    print ("O valor está entre os decibéis do cortador de grama e do despertador. ")
elif db < despertador and db > sala:
    print ("O valor está entre os decibéis do despertador e da sala silenciosa. ")
elif db > britadeira:
    print ("O valor é maior que os decibéis da britadeira. ")
elif db < sala:
    print ("O valor é menor que os decibéis da sala silenciosa. ")