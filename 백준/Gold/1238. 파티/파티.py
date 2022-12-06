import sys,heapq
INF = sys.maxsize
n,m,x = map(int,input().split())
graph = {i+1:[] for i in range(n)}
temp = {i+1:[] for i in range(n)}
res = []
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[b].append([a,c])
    temp[a].append([b,c])

def dijkstra(start):
    global res
    d = [INF for _ in range(n + 1)]
    d[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    res.append(d[1:])

dijkstra(x)
graph = temp
dijkstra(x)
max_ = 0
for i in range(n):
    max_ = max(max_,res[0][i]+res[1][i])
print(max_)