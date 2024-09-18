def uniquechars(str):
    str2 = {}
    for letra in str:
        if letra in str2:
            return False
        else:
            str2[letra] = 1
    return True


#main
str = input("Digite a string: ")
x = uniquechars(str)
print (x)