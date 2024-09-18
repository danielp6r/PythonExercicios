tokens = []
token = ""
operador = ""
anterior = []

string1 = ("(+80) * (-60) + (-100) / - (-10)") 
expressao = string1.replace(" ", "") 
for c in expressao:
    if c == "*" or c == "/" or c == "^" or c == "(" or c == ")":
        if token != '':
            tokens.append(token)
            token = ""
        tokens.append(c)
    elif c == "+" or c == "-" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or c == "0":
        if c [-1] == "-":
            anterior.append(c)
            token += c
        elif c [-1] == "+":
            c.replace ("+", "")
            anterior.append(c)
        elif c [-1] == "*" or c [-1] == "/" or c [-1] == "^":
            anterior.append(c)
            tokens.append(c)
        elif c == 1 or c == 2 or c == 3 or c == 4 or c == 5 or c == 6 or c == 7 or c == 8 or c == 9 or c == 0:
            anterior.append(c)
            token += c
        else:
            token += c
            
print (expressao)        
print (tokens)