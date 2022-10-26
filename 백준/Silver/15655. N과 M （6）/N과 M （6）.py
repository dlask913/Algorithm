n,m=map(int,input().split())
lst = [0 for _ in range(n+1)]
n_value = list(map(int,input().split()))
n_value.sort()
def NnM(lev):
    if lev >= m:
        if len(set(lst[:m])) == m and sorted(lst[:m])==lst[:m]:
            for i in range(m):
                print(lst[i], end=' ')
            print()
        return
    for i in n_value:
        lst[lev] = i
        NnM(lev+1)
NnM(0)
