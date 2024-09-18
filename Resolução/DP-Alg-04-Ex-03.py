x = 0
print ('Celsius/Fahrenheit:')
for i in range (0,101, 10):
    print(i,'ºC\t',end="")
    x = i * 1.8 + 32
    print (f' {x:.0f} ºF')
    