def hextoint(hexnum):
    hexnum = hexnum.upper()
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decnum = 0
    for i in range(len(hexnum)):
        decnum += hex_dict[hexnum[i]] * 16 ** (len(hexnum) - i - 1)
    return decnum

def inttohex(decnum):
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexnum = ''
    while decnum > 0:
        hexnum = hex_dict[decnum % 16] + hexnum
        decnum = decnum // 16
    return hexnum


#main
hexnum = input("Digite um número hexadecimal: ")
x = hextoint(hexnum)
print("O número hexadecimal {} corresponde ao número decimal {}".format(hexnum, x))

#main2
decnum = int(input("Digite um número decimal: "))
y = inttohex(decnum)
print("O número decimal {} corresponde ao número hexadecimal {}".format(decnum, y))