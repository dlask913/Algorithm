import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
m,n,k=map(int,input().split())
graph=[[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
cnt = 1
res = []
def draw(x1,y1,x2,y2):
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=-1

def dfs(x,y):
    global cnt
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 0:
            visited[nx][ny] = 1
            graph[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)

for _ in range(k):
    a,b,c,d=map(int,input().split())
    draw(a,b,c,d)

for i in range(m):
    for j in range(n):
        if graph[i][j]==0 and visited[i][j]==0:
            graph[i][j]=1
            dfs(i,j)
            res.append(cnt)
            cnt = 1

print(len(res))
res.sort()
for i in res:
    print(i,end=' ')