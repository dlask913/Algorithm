import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
graph = []
dq = deque()

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def bfs(dq,graph,n,m,cnt):
    dw = [0, -1, 1, 0]
    dh = [-1, 0, 0, 1]
    while dq:
        for _ in range(len(dq)):
            x,y = dq.popleft()
            for i,j in zip(dh,dw):
                dx,dy=x+i,y+j
                if 0<=dx<n and 0<=dy<m and graph[dx][dy]==0:
                    graph[dx][dy]=1
                    dq.append((dx,dy))
        cnt += 1

    if any(0 in l for l in graph): print(-1)
    else: print(cnt)

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            dq.append((i,j))

bfs(dq,graph,n,m,-1)