def maxCross(arr, left, mid, right):
    Sum = 0
    sumL = arr[mid]
    maxL = mid
    for i in range(mid, left - 1, -1):
        Sum += arr[i]
        if (Sum > maxL):
            sumL = Sum
            maxL = i
    Sum = 0
    sumR = arr[mid + 1]
    maxR = mid + 1
    for j in range(mid + 1, right + 1):
        Sum += arr[j]
        if (Sum > sumR):
            sumR = Sum
            maxR = j
    Sum = sumL + sumR
    return maxL, maxR, Sum

def maxCross2(arr, left, mid, right):
    maxL = mid
    sumL = arr[mid]
    Sum = 0
    for i in range(mid, left + 1, - 1):
        Sum += arr[i]
        if Sum > sumL: 
            sumL = Sum
            maxL = i
    maxR = mid + 1
    sumR = arr[mid + 1]
    Sum = 0
    for j in range(mid + 1, right + 1):
        Sum += arr[j]
        if Sum > sumR:
            sumR = Sum
            maxR = j
    Sum = sumL + sumR
    return maxL, maxR, Sum

def maxSubArray(arr, left, right):
    if (left == right):
        return left, right, arr[left]
    else:
        mid = (left + right) // 2
        leftL, rightL, sumL = maxSubArray(arr, left, mid)
        leftR, rightR, sumR = maxSubArray(arr, mid + 1, right)
        leftX, rightX, sumX = maxCross(arr, left, mid, right)
        if ((sumL >= sumR) and (sumL >= sumX)):
            return leftL, rightL, sumL
        elif((sumR >= sumR) and (sumR >= sumX)):
            return leftR, rightR, sumR
        else:
            return leftX, rightX, sumX

def maxSubArray2(arr, left, right):
    if left == right:
        return left, right, arr[left]
    else:
        mid = (left + right) // 2
        leftL, rightL, sumL = maxSubArray2(arr, left, mid)
        leftR, rightR, sumR = maxSubArray2(arr, mid + 1, right)
        leftX, rightX, sumX = maxCross2(arr, left, mid, right)

        if sumL > sumR and sumL > sumX:
            return leftL, rightL, sumL
        if sumR > sumL and sumR > sumX:
            return leftR, rightR, sumR
        else:
            return leftX, rightX, sumX

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(maxSubArray2(arr, 0, len(arr) - 1))
