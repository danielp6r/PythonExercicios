def palindromo(s):
    s2 = s.replace(' ', '')
    if s2=="":
        return True
    elif len(s) == 1:
        return True
    elif (s2[0]==s2[-1]) and palindromo(s2[1:-1]):
        return True
    else:
        return False


#main
s = input("Digite uma string: ")
print(palindromo(s))