def df(M={}, N={}):
    x = []
    for i in M:
        if i not in N:
            x.append(i)
    for i in N:
        if i not in M:
            x.append(i)
    x = sorted(x)
    return x


#main
M = {2, 4, 5, 9}
N = {2, 4, 11, 12}
print(df(M, N))    