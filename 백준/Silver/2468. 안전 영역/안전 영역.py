import copy,sys
sys.setrecursionlimit(10000)
n = int(input())
reg = []
res = 0
for _ in range(n):
    reg.append(list(map(int,input().split())))
max_ = max(map(max,reg))


def search(depth,visited):
    global res
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]>depth:
                cnt += 1
                dfs(i,j,depth)
    res = cnt if cnt> res else res

def dfs(x,y,depth):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[x][y]=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > depth:
            visited[nx][ny] = 0
            dfs(nx,ny,depth)

for i in range(max_+1):
    visited = copy.deepcopy(reg)
    search(i,visited)

print(res)