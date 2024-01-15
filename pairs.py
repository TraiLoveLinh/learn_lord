def pairs(k, arr):
    d = Counter(arr)
    pairs = 0
    for i in arr:
        if i + k in d:
            pairs += 1
        if i - k in d:
            pairs += 1
        del d[i]
    return pairs