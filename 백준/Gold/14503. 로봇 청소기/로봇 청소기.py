n,m = map(int,input().split())
r,c,d = map(int,input().split())
room = []
v = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 1
for _ in range(n):
    room.append(list(map(int,input().split())))

def direction_change(d):
    if d==0: return 3
    elif d==1: return 0
    elif d==2: return 1
    elif d==3: return 2

v[r][c] = 1
cnt = 0
while True:
    d = direction_change(d)
    nx, ny = dx[d] + r, dy[d] + c
    if room[nx][ny] == 0 and v[nx][ny] == 0:
        v[nx][ny] = 1
        ans += 1
        r, c = nx, ny
        cnt = 0
        continue
    else:
        cnt += 1

    if cnt == 4:
        nx,ny = r-dx[d], c-dy[d]
        if room[nx][ny] == 1:
            break
        r,c = nx,ny
        cnt = 0

print(ans)
