n = int(input())
a = list(input().split(","))
for b in a:
    k = len(b)
    x = 0
    for i in range(k):
        x += int(b[i])*2**(k-i-1)
    if (x % 5 == 0):
        print(b)
