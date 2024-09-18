def raizrec(n,estimativa=1.0):
    if abs(estimativa**2 - n) <= 1e-13:
        return estimativa
    else:
        estimativa = (estimativa+ (n/estimativa))/2
        return raizrec(n,estimativa)


#main
n = float(input("Digite um número: "))
print ("A raiz quadrada de",n,"é",raizrec(n))