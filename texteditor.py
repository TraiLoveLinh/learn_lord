Q = int(input())
queue = []
s = []
for _ in range(Q):
    inp = input().split()
    if inp[0] == '1':
        for ch in inp[1]:
            s.append(ch)
        queue.append(['1',len(inp[1])])
    elif inp[0] == '2':
        k = int(inp[1])
        queue.append(['2',s[-k:]])
        del s[-k:]
    elif inp[0] == '3':
        k = int(inp[1])
        print(s[k-1])
    else:
        last = queue[len(queue) - 1]
        if last[0] == '1':
            del s[-last[1]:]
            del queue[len(queue) - 1]
        else:
            for ch in last[1]:
                s.append(ch)
            del queue[len(queue) - 1]


