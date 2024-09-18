posição = input("Digite uma posição. ")
if posição [0] == ("a") or posição [0] == ("c") or posição [0] == ("e") or posição [0] == ("g"):
    coluna = "preta"
else :
    coluna = "branca"
if posição [1] == ("1") or posição [1] == ("3") or posição [1] == ("5") or posição [1] == ("7"):
    linha = "preta"
else :
    linha = "branca"
if coluna != linha:
    print ("A posição é branca. ")
else :
    print ("A posição é preta. ")