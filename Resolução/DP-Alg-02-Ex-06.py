x = int(input("Digite um número inteiro de 4 dígitos. "))
a = x // 1000
ra = x % 1000
b = ra // 100
rb = ra % 100
c = rb // 10 
rc = rb % 10
d = rc // 1 
print ("A soma dos dígitos dos números é: ",a + b + c + d)