from collections import deque

def bfs(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    n,m= len(maps)-1,len(maps[0])-1
    v = [[0 for _ in range(m+1)] for _ in range(n+1)]
    v[0][0] = 1
    q = deque()
    q.append((0,0,1))
    while q:
        x,y,c = q.popleft()
        if x==n and y==m:
            return c
        v[x][y]=1
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<=n and 0<=ny<=m and maps[nx][ny]==1 and v[nx][ny]==0:
                v[nx][ny]=1
                q.append((nx,ny,c+1))
    return -1
def solution(maps):
    ans = bfs(maps)
    return (ans)