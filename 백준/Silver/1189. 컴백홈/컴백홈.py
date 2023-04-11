r,c,k = map(int,input().split())
load = []
v = [[0 for _ in range(c)] for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = []
for _ in range(r):
    load.append(list(input()))

def backTracking(x,y,cost):
    if x==0 and y==(c-1):
        ans.append(cost)
        return
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and v[nx][ny]==0 and load[nx][ny] != 'T':
            cost += 1
            v[nx][ny] = 1
            backTracking(nx,ny,cost)
            cost -= 1
            v[nx][ny] = 0

v[r-1][0]=1
backTracking(r-1,0,1)
print(ans.count(k))