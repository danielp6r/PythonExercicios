def anagrama(s1, s2):
    if s1 == s2:
        return False
    elif len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


#main
s1 = input("Digite a primeira palavra: ")
s2 = input("Digite a segunda palavra: ")
print(anagrama(s1, s2))