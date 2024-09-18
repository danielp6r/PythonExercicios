def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)


#main
n = int(input("Digite um número: "))
print(fatorial(n))