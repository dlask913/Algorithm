from collections import deque
n,m = map(int,input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
picture = []
ans,cnt = 0,0
for _ in range(n):
    picture.append(list(map(int,input().split())))

def bfs(a,b,v):
    dx,dy = [0,0,-1,1],[1,-1,0,0]
    q = deque([(a,b)])
    v[a][b] = 1
    c = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and picture[nx][ny]==1 and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx,ny))
                c += 1
    return c

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and visited[i][j] == 0:
            ans = max(bfs(i,j,visited),ans)
            cnt += 1

print(cnt)
print(ans)

