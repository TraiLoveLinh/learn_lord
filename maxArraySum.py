import numpy as np

def maxSubsetSum(arr: list)->int:
    dp = [0]*(len(arr)+1)
    dp[1] = arr[0]

    for i in range(2, len(arr)+1):
        dp[i] = max(dp[i-1], max(arr[i-1], dp[i-2] +  arr[i-1]))
        
    print(dp)
    return dp[len(arr)]
# an 10 elements array in range of [-10,10]
arr = [np.random.randint(-10, 10) for _ in range(10)]


print(arr)
maxSubsetSum(arr)
