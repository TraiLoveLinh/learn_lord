def asp(start, finish):
    result = [0]
    i = 0
    for j in range(1, len(start)):
        if start[j] >= finish[i]:
            result.append(j)
            i = j
    return result


if __name__ == '__main__':
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 10, 11, 12, 14, 16]
    A = asp(s, f)
    print(A)
