def dist(dpkm):
    return 4 + 0.25 * 1000/140 * dpkm
     

# main
dp = float(input("Digite a distância percorrida em km: "))
x = dist(dp)
print(f"O valor da viagem é: R$ {x:,.2f}")