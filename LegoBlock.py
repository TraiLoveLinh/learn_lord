mod = 10**9+7

# n is height and m is width
def legoBlocks(n, m):
    valid =[0,1,2,4,8]
    total =[0]
    result=[0]
    for i in range(1,m+1):
        if i>=5:
            valid.append((valid[i-1]+valid[i-2]+valid[i-3]+valid[i-4])%mod)
        tem=1
        for j in range(n):
            tem *= valid[i]
            tem%= mod
        total.append(tem)
    
    for i in range(1,m+1):
        result.append(total[i])
        for j in range(i+1):
            result[i] += mod
            result[i] -= (result[j]*total[i-j])%mod
    return result[m]%mod