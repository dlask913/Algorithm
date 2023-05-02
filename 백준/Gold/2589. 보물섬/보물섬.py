from collections import deque
n,m = map(int,input().split())
land = []
ans = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(n):
    land.append(list(input()))

def bfs(a,b):
    global ans
    v = [[0 for _ in range(m)] for _ in range(n)]
    v[a][b] = 1
    q = deque()
    q.append((a,b,0))
    res = 0
    while q:
        for _ in range(len(q)):
            x,y,cost = q.popleft()
            res = res if cost < res else cost
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and v[nx][ny] == 0 and land[nx][ny]=='L':
                    v[nx][ny]=1
                    q.append((nx,ny,cost+1))
    ans.append(res)


for i in range(n):
    for j in range(m):
        if land[i][j] == 'L':
            bfs(i,j)
print(max(ans))