def decodif(comp):
    if len(comp) < 2:
        return comp
    c = comp[0]
    n = comp[1]
    if n.isdigit():
        return c * int(n) + decodif(comp[2:])
    else:
        return c + decodif(comp[1:])


#main
x = decodif("a6b2a6b1") 
print(x)