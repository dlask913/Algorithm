import sys,heapq
n,e=map(int,sys.stdin.readline().split())
graph=[[]for _ in range(n+1)]
INF=sys.maxsize
d=[INF for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v,w=map(int,sys.stdin.readline().split())

def dijkstra(start,end):
    d = [sys.maxsize for _ in range(n + 1)]
    d[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if d[i[0]]>cost:
                d[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return d[end]
sol = min(dijkstra(1,v)+dijkstra(w,n),dijkstra(1,w)+dijkstra(v,n))+dijkstra(v,w)
if sol >= INF:
    print(-1)
else:
    print(sol)
