import math
from collections import deque
n,l,r = map(int,input().split())
land = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
for _ in range(n):
    land.append(list(map(int,input().split())))

def bfs(a,b):
    dq = deque()
    g = deque()
    dq.append((a,b))
    g.append((a,b))
    v[a][b] = 1
    s = land[a][b]
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<n and l<=abs(land[x][y]-land[nx][ny])<=r and v[nx][ny] == 0:
                v[nx][ny] = 1
                s += land[nx][ny]
                dq.append((nx,ny))
                g.append((nx,ny))
    for i,j in g:
        land[i][j] = math.floor(s / len(g))
    return len(g)

ans = 0
while True:
    f = True
    v = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                if bfs(i,j) > 1:
                    f = False
    if f:
        print(ans)
        break
    ans += 1