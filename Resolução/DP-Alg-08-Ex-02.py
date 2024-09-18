def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


#main
n = int(input("Digite um número: "))
print ("O número {} da sequencia fibonacci é {}".format(n, fibonacci(n)))