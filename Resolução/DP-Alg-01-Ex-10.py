from math import log10


a = int (input ("digite o valor de a. "))
b = int (input ("digite o valor de b. "))
soma = int (a + b)
diferenca = int (- b + a) 
produto = int (a * b) 
quociente = int (a / b)
resto = (a % b) 
log10a = log10(a) 
res_axxb = (a**b)
print ("A soma de a e b é", soma , '.')
print ("A diferença de b - a é", diferenca , '.')
print ("O produto de a por b é", produto , '.')
print ("O quociente de a / b é", quociente , '.')
print ("O resto da divisão a / b é", resto , '.')
print ("O resultado do log10a é", log10a , '.')
print ("O resultado de a elevado a b é", res_axxb , '.')