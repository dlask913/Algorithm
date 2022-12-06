import sys
input = sys.stdin.readline
n,m=map(int,input().split())
lst = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = 0
for _ in range(n):
    lst.append(list(map(int,input().split())))
def bruteforce(x,y,c,d):
    global res
    if d>=3:
        res = max(res,c)
        return
    temp = lst[x][y]
    min_ = 1000
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and v[nx][ny]==0:
            v[nx][ny]=1
            bruteforce(nx,ny,c+lst[nx][ny],d+1)
            min_ = min(min_, lst[nx][ny])
            temp += lst[nx][ny]
            v[nx][ny]=0
    if 0<x<(n-1) and 0<y<(m-1):
        temp -= min_
    res = max(res,temp)

v=[[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        v[i][j]=1
        bruteforce(i,j,lst[i][j],0)
        v[i][j]=0
print(res)