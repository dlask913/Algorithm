import sys
sys.setrecursionlimit(10000)
n = int(input())
lst = []
dp = [[0 for _ in range(n)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(n):
    lst.append(list(map(int,input().split())))

def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y]=1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and lst[nx][ny] < lst[x][y]:
            dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

for i in range(n):
    for j in range(n):
        dfs(i,j)

print(max(map(max,dp)))