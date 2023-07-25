def solution(x, y, n):
    answer = 0
    INF = int(1e9)
    d = [INF for _ in range(y+1)]
    d[x] = 0
    for i in range(x,y+1):
        if d[y]<INF: break
        for j in (i+n,i*2,i*3):
            if j>y:
                continue
            d[j] = min(d[j],d[i]+1)
    
    return d[y] if d[y]<INF else -1