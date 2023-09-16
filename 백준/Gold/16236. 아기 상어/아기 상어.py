n = int(input())
space = []
shark = () # (크기,x,y)
q = []
res = 0
feed = 0

for _ in range(n):
    space.append(list(map(int,input().split())))

def find_fish(feed,shark,q):
    global res
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    v = [[0 for _ in range(n)] for _ in range(n)] # 방문 처리
    t = 0 # 시간
    v[shark[1]][shark[2]] = 1
    while q:
        for _ in range(len(q)):
            x,y = q.pop(0)
            if 0 < space[x][y] < shark[0]:
                res += t
                feed += 1
                space[x][y] = 0

                if feed == shark[0]:
                    feed = 0
                    shark = (shark[0]+1,x,y)
                else:
                    shark = (shark[0],x,y)
                q = [(x,y)]
                return find_fish(feed,shark,q)

            for i in range(4):
                nx,ny=dx[i]+x,dy[i]+y
                if 0<=nx<n and 0<=ny<n and space[nx][ny] <= shark[0] and v[nx][ny] == 0:
                    q.append((nx,ny))
                    v[nx][ny] = 1
        t += 1
        q.sort()
    return -1

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark = (2,i,j)
            q.append((i,j))
            space[i][j] = 0
            break

find_fish(feed,shark,q) 
print(res)