import sys,heapq
INF = sys.maxsize
n,m = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
d=[INF for _ in range(n+1)]
start = int(sys.stdin.readline())

for i in range(m):
    x,y,c = map(int,sys.stdin.readline().split())
    graph[x].append([y,c])
    
def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if d[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,n+1):
    if d[i] == INF:
        print("INF")
    else:
        print(d[i])
