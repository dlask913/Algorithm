import sys
n,m=map(int,sys.stdin.readline().split())
lst =[]
dp= [[-1 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(x,y):
    if x==0 and y==0:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y]=0
    for i,j in zip(dx,dy):
        if 0<=(x+i)<n and 0<=(y+j)<m and lst[x][y] < lst[x+i][y+j]:
            dp[x][y] += dfs(x+i,y+j)
    return dp[x][y]

print(dfs(n-1,m-1))
