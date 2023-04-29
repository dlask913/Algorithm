from collections import deque
r,c = map(int,input().split())
maze = []
fire_check = [[0 for _ in range(c)] for _ in range(r)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q = deque()
fire = deque()
res = 0
for _ in range(r):
    maze.append(list(input()))

def bfs():
    global res
    if not q:
        res = -1
        return
    for _ in range(len(q)):
        x, y, cnt = q.popleft()
        res = cnt if cnt > res else res
        if maze[x][y] == 'F':
            continue
        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            res += 1
            return

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == '.' and maze[nx][ny] != 'F':
                maze[nx][ny] = 'J'
                q.append((nx,ny,cnt+1))

    for _ in range(len(fire)):
        x, y = fire.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<= nx <r and 0 <= ny <c and maze[nx][ny] != '#' and fire_check[nx][ny] == 0:
                fire_check[nx][ny] = 1
                maze[nx][ny] = 'F'
                fire.append((nx,ny))
    bfs()

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            q.append((i,j,0))
        if maze[i][j] == 'F':
            fire.append((i,j))
            fire_check[i][j] = 1
bfs()

if res == -1:
    print("IMPOSSIBLE")
else:
    print(res)