from collections import deque
n,k= map(int,input().split())
d= [0 for _ in range(100001)]
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        dx=[x-1,x+1,x*2]
        if x==k:
            print(d[x])
            break
        for i in dx:
            if 0<= i <= 100000 and not d[i]:
                d[i] = d[x]+1
                q.append(i)
bfs()
