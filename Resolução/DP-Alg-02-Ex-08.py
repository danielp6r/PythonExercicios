n = int(input("Digite um número inteiro de 3 algarismos. "))
c = n // 100
rc = n % 100
d = rc // 10
rd = rc % 10
u = rd // 1
m = u * 100 + d * 10 + c
print (m)