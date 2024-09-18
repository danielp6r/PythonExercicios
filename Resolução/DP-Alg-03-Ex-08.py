nota = input("Digite o nome de uma nota musical. ")
if nota [0] == "c":
    print ("A frequência dessa nota é", 261.63 / 2 ** (4 - int (nota[1])), "Hz. ")
elif nota [0] == "d":
    print ("A frequência dessa nota é", 293.66 / 2 ** (4 - int (nota[1])), "Hz. ")
elif nota [0] == "e":
    print ("A frequência dessa nota é", 329.63 / 2 ** (4 - int (nota[1])), "Hz. ")
elif nota [0] == "f":
    print ("A frequência dessa nota é", 349.23 / 2 ** (4 - int (nota[1])), "Hz. ")
elif nota [0] == "g":
    print ("A frequência dessa nota é", 392.00 / 2 ** (4 - int (nota[1])), "Hz. ")
elif nota [0] == "a":
    print ("A frequência dessa nota é", 440.00 / 2 ** (4 - int (nota[1])), "Hz. ")
elif nota [0] == "b":
    print ("A frequência dessa nota é", 493.88 / 2 ** (4 - int (nota[1])), "Hz. ")