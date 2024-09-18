def isInteger(string):
    string2 = string.strip()
    if string2[0] == "+" or string2[0] == "-":
        string2 = string2[1:]
    if string2.isdigit():
        return True
    else:
        return False

#main
string = input("Digite a string: ")
if isInteger(string):
    print("A string é um número inteiro.")
else:
    print("A string não é um número inteiro.")