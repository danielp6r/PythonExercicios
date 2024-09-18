x = int(input("Digite a quantidade de centavos a serem devolvidos. "))
moeda50 = x // 50
resto50 = x % 50
moeda25 = resto50 // 25
resto25 = resto50 % 25
moeda10 = resto25 // 10
resto10 = resto25 % 10
moeda5 = resto10 // 5
resto5 = resto10 % 5
moeda1 = resto5 // 1
print ("Moedas de 50 centavos devolvidas: ", moeda50)
print ("Moedas de 25 centavos devolvidas: ", moeda25)
print ("Moedas de 10 centavos devolvidas: ", moeda10)
print ("Moedas de 05 centavos devolvidas: ", moeda5)
print ("Moedas de 01 centavo devolvidas:  ", moeda1)