def anagramadefrases(frase1, frase2):
    frase1 = frase1.replace(" ", "").lower()
    frase2 = frase2.replace(" ", "").lower()
    if len(frase1) != len(frase2):
        return False
    elif frase1 == frase2:
        return False
    s1 = sorted(frase1)
    s2 = sorted(frase2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


#main
frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")
print (anagramadefrases(frase1, frase2))