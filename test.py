ans = 0
def targetCross(arr, left, mid, right, target):
    global ans

    Sum = 0
    sumL = arr[mid]
    for i in range(mid, left - 1, -1):
        Sum += arr[i]
        if (Sum == target):
            ans += 1
    Sum = 0
    sumR = arr[mid + 1]
    for j in range(mid + 1, right + 1):
        Sum += arr[j]
        if (Sum == target):
            ans += 1
    Sum = sumL + sumR
    if Sum == target:
        ans += 1
    return Sum

def targetSubArray(arr, left, right, target):
    if (left == right):
        if (arr[left] == target):
            global ans
            ans += 1
    else:
        # global ans
        mid = (left + right) // 2
        sumL = targetSubArray(arr, left, mid, target)
        sumR = targetSubArray(arr, mid + 1, right, target)
        sumX = targetCross(arr, left, mid, right, target)
        if sumL == target:
            ans += 1
            return sumL
        if sumR == target:
            ans += 1
            return sumR
        if sumX == target:
            ans += 1
            return sumX


arr = [4,4]
print(targetSubArray(arr, 0, len(arr) - 1, 4))
print(ans)
