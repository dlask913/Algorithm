import copy
import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
graph = []
dq = deque()
cnt = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(dq, visited):
    dw = [0, -1, 1, 0]
    dh = [-1, 0, 0, 1]
    for i in range(n):
        for j in range(m):
            if visited[i][j]==2:
                dq.append((i,j))
    while dq:
        x,y = dq.popleft()
        for i,j in zip(dh,dw):
            dx,dy=x+i,y+j
            if 0<=dx<n and 0<=dy<m and visited[dx][dy]==0:
                visited[dx][dy]=2
                dq.append((dx,dy))
    temp = 0
    for i in visited:
        temp+=i.count(0)
    cnt.append(temp)

def bruteforce(visited, c):
    if c >= 3:
        visited = copy.deepcopy(graph)
        bfs(dq,visited)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                bruteforce(graph, c + 1)
                graph[i][j]=0

bruteforce(graph, 0)
print(max(cnt))