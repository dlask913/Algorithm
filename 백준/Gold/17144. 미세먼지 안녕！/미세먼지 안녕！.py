from collections import deque
r,c,t = map(int,input().split())
a = []
m = deque() # 공기청정기 위치

for _ in range(r):
    a.append(list(map(int,input().split())))

def air_cleaner(x,y,dx,dy,l1,l2): # 공기 청정기
    global a
    d = 0
    while True:
        if a[x][y] == -1:
            return
        nx,ny = dx[d%4]+x,dy[d%4]+y
        if l1<=nx<l2 and 0<=ny<c:
            if a[nx][ny] == -1:
                break
            a[x][y] = a[nx][ny]
            x,y = nx,ny
        else:
            d += 1

def bfs(q,a,m): # 미세먼지 확산
    dx = [0, 0, 1, -1]  # 오른, 왼, 위, 아래
    dy = [1, -1, 0, 0]
    room = [[0 for _ in range(c)] for _ in range(r)]
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            cnt = 0
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<r and 0<=ny<c and a[nx][ny] != -1:
                    room[nx][ny] += (a[x][y]//5)
                    cnt += a[x][y] // 5
            room[x][y] -= cnt
    for i in range(r):
        for j in range(c):
            a[i][j] += room[i][j]

    air_cleaner(m[0][0]-1,m[0][1],[-1,0,1,0],[0,1,0,-1],0, m[0][0]+1) # 위 = 위 -> 오른 -> 아래 -> 왼
    air_cleaner(m[1][0]+1,m[1][1],[1,0,-1,0],[0,1,0,-1],m[1][0], r) # 아래 = 아래 -> 오른 -> 위 -> 왼
    a[m[0][0]][1],a[m[1][0]][1] = 0,0 # 공기 청정기 오른쪽


for i in range(r):
    if a[i][0] == -1:
        m.append((i,0))

for _ in range(t):
    q = deque()
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                q.append((i,j))
    bfs(q,a,m)

print(sum(sum(a,[]))+2)