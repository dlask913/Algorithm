from collections import deque
dx,dy = [0,0,0,-1,1],[0,1,-1,0,0]
n,k = map(int,input().split())
board = []
horse = {}
stat = {}
def change(lev): # 방향 변경
    if lev % 2 == 0:
        return lev-1
    else:
        return lev+1
def horses(x,y,stat,cur): # 움직여야하는 말들 담기
    tmp = deque()
    l = len(stat[(x, y)])
    for _ in range(l):  # (x,y) 좌표에 있는 말들 앞에서부터
        num, direct = stat[(x, y)].pop()
        tmp.appendleft((num, direct))
        if num == cur:
            break
    return tmp

def move(tmp,flag,x,y,cur): # 움직이기 ( 좌표 업데이트 )
    global horse
    while tmp:
        num, direct = tmp.popleft()
        if flag and cur == num: # 파란색일 때 방향 변경
            direct = change(direct)
        if (x, y) not in stat:
            stat[(x, y)] = [(num, direct)]
        else:
            stat[(x, y)].append((num, direct))
        horse[num] = (x, y, direct)

for _ in range(n):
    board.append(list(map(int,input().split())))

for j in range(1,k+1): # 좌표 입력 받고 현재 위치&방향 저장
    x,y,d = map(int,input().split())
    horse[j] = (x-1, y-1, d)
    stat[(x-1,y-1)] = [(j,d)]

cnt = 0
flag = True
while flag:
    if cnt >= 1000:
        cnt = -1
        break
    for i in range(1,k+1):
        x,y,d = horse[i]
        tmp = horses(x,y,stat,i)
        blue = False
        nx,ny = x+dx[d], y+dy[d]

        if 0 > nx or n <= nx or 0 > ny or n <= ny or board[nx][ny] == 2: # 첨에 파랑일 때
            blue = True
            d = change(d)
            nx,ny = x+dx[d],y+dy[d]

        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0: # 흰 색(이동)
            x,y = nx,ny
        elif 0<=nx<n and 0<=ny<n and board[nx][ny] == 1: # 빨강(이동 후 거꾸로)
            tmp.reverse()
            x,y = nx,ny

        move(tmp, blue, x, y, i)

        if len(stat[(x,y)]) >= 4: # 현재 말이 4개 이상이면 종료
            flag = False
            break
    cnt += 1

print(cnt)