INF = float("inf")
def coinChange(n):
    F = [0] * (n + 1)
    for i in range(1, n + 1):
        temp = INF
        j = 0
        while j < m and C[j] <= n:
            temp = min(1 + F[n - C[j]], temp)
            j = j + 1
            F[i] = temp
    return F
def coin_change2(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    return dp[target]

C = [1,3,4]
m = len(C)
n = 6
print(coinChange(n))
print(coin_change2(C, n))
