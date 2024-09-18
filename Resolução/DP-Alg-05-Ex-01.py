import math

def hipotenusa(lado1, lado2):
    h = math.sqrt(lado1**2 + lado2**2)
    return h

def main():
    l1 = float(input("Digite o valor do primeiro lado: "))  
    l2 = float(input("Digite o valor do segundo lado: "))
    x = hipotenusa(l1, l2)
    print("O valor da hipotenusa é: ", x)

if __name__ == "__main__":
    main()