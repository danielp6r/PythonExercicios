pre_calculados = {0:0, 1:1} 
def fibonacci(n):
    if n in pre_calculados: 
        return pre_calculados[n]
    res = fibonacci(n-1) + fibonacci(n-2) 
    pre_calculados[n] = res
    return res


#main
n = int(input("Digite um número: "))
print ("O número {} da sequencia fibonacci é {}".format(n, fibonacci(n)))