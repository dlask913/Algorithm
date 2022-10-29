tc = int(input())
INF = int(100000)
def bellman_ford():
    d = [INF for _ in range(n + 1)]
    d[1] = 0
    for k in range(n):
        for i in range(1,n+1):
            for j in graph[i]:
                if d[i]+j[1] < d[j[0]]:
                    d[j[0]] = d[i]+j[1]  
                    if k == n-1:
                        return True
    return False


for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = {i+1:[] for i in range(n)}
    for _ in range(m):
        s,e,t = map(int,input().split())
        graph[s].append([e,t])
        graph[e].append([s,t])
    for _ in range(w):
        s,e,t=map(int,input().split())
        graph[s].append([e,-t])
    if bellman_ford(): print("YES")
    else: print("NO")