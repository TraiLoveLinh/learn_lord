def maximaSet(P):
    if (len(P) < 2):
        return set(P)
    else:
        mid = len(P) // 2
        p = P[mid] 
        L = [x for x in P if x[0] < p[0]]
        R = [x for x in P if x[0] >= p[0]]
        ML = maximaSet(L)
        MR = maximaSet(R)
        q = min(list(MR))
        AML = list(ML)
        for p in AML:
            if p[0] <= q[0] and p[1] <= q[1]:
                ML.remove(p)
        return ML | MR

P = [(7,2),(3,1),(9,3),(4,5),(1,4),(6,9),(2,6),(5,7),(8,6)]
print(maximaSet(P))
