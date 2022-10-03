n,m=map(int,input().split())
lst = [0 for _ in range(n+1)]

def NnM(lev):
    if lev >= m:
        for i in range(m):
            print(lst[i], end=' ')
        print()
        return
    for i in range(1,n+1):
        lst[lev] = i
        NnM(lev+1)
NnM(0)
