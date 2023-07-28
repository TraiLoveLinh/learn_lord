def changeMoney(M, C):
    n = len(C)
    k = n - 1
    x = [0] * n
    while (k >= 0 and M > 0):
        x[k] = M // C[k]
        M = M % C[k]
        k -= 1
    return x

C = [1,2,5,10]
M = 9
print(changeMoney(M, C))

