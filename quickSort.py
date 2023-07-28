def partition(arr, left, right):
    i = left
    p = i
    pivot = arr[p]
    for j in range(left + 1, right + 1):
        if (arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i

def quickSort(arr, left, right):
    if (left < right):
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot - 1)
        quickSort(arr, pivot + 1, right)

arr = [1,2,9,4,8,1,7,4,9,8,2]
quickSort(arr, 0, len(arr) - 1)
print(arr)
