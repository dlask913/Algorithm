""" 브루트포스 """
import copy
n = int(input())
hall = [] # 복도( S: 학생, T: 선생, O: 장애물 )
v = [[0 for _ in range(n)] for _ in range(n)] # 방문 체크 용
T = [] # 선생님 위치
res = 1
for _ in range(n):
    hall.append(list(input().split()))

def bruteforce(lev,v): # (행,열,장애물 개수,방문)
    global res
    if lev == 3: # 장애물 3개 다 두고 check()로 발견된 학생 수 받아 저장
        if check(v):
            res = 0
        return
    for i in range(n):
        for j in range(n):
            if hall[i][j] == 'X' and v[i][j] == 0:
                v[i][j] = 1 # 장애물 두기
                bruteforce(lev+1,v)
                v[i][j] = 0

def check(v): # 감시 가능한 학생 수
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    q = copy.deepcopy(T)
    cnt = 0
    while q:
        x,y = q.pop()
        for d in range(4):
            for i in range(1,n+1):
                nx,ny = x+dx[d]*i, y+dy[d]*i
                if 0<=nx<n and 0<=ny<n and v[nx][ny] == 0:
                    if hall[nx][ny] == 'S':
                        cnt += 1
                else: # 범위 벗어나거나 장애물인 경우
                    break

    return False if cnt != 0 else True

for i in range(n):
    for j in range(n):
        if hall[i][j] == 'T':
            T.append((i,j))

bruteforce(0,v)

if res == 0:
    print("YES")
else:
    print("NO")
