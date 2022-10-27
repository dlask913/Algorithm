from collections import deque
n,m=map(int,input().split())
graph=[]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
res = []
for _ in range(n):
    graph.append(list(input()))

def bfs():
    q = deque()
    q.append((0, 0, 0)) # 현재 위치 + 벽을 부신 여부
    v = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    v[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        if x==(n-1) and y==(m-1):
            return v[n-1][m-1][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == '0' and v[nx][ny][z]==0:
                    v[nx][ny][z]=v[x][y][z]+1
                    q.append((nx,ny,z))
                elif graph[nx][ny] =='1' and z==0:
                    v[nx][ny][1] = v[x][y][0]+1
                    q.append((nx,ny,1))
    return -1

print(bfs())
