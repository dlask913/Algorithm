from collections import deque
m,n = map(int,input().split())
castle = []
v = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [0,-1,0,1],[-1,0,1,0]
room = {} # (고유 넘버, 넓이)
num = 1 # 방 넘버
# 남쪽 동쪽 북쪽 서쪽 ( 1 1 1 1 )
for _ in range(n):
    castle.append(list(map(int,input().split())))


def bfs(tx,ty,c): # 넓이 계산
    global room
    q = deque([])
    q.append((tx, ty))
    v[tx][ty] = c
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and v[nx][ny] == 0:
                if not castle[x][y] & (1 << i): # i 쪽 벽이 없다면
                    v[nx][ny] = c
                    q.append((nx,ny))
                    cnt += 1
    room[c] = cnt


for i in range(n):
    for j in range(m):
        if v[i][j] == 0:
            room[num] = 1
            bfs(i,j,num)
            num += 1

res = min(room.values())
for i in range(n):
    for j in range(m):
        for k in range(4):
            nx,ny = i+dx[k], j+dy[k]
            if 0<=nx<n and 0<=ny<m and v[i][j] != v[nx][ny]: # 인접한 방들 중 넓이 값 갱신
                res = max(res, room[v[i][j]] + room[v[nx][ny]])

print(len(room))
print(max(room.values()))
print(res)