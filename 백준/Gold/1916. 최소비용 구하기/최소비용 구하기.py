import sys,heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
d=[sys.maxsize for _ in range(n+1)]

for _ in range(m):
    x,y,c = map(int,sys.stdin.readline().split())
    graph[x].append([y,c])
start,end = map(int,sys.stdin.readline().split())
d[start]=0

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<d[i[0]]:
                d[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
print(d[end])