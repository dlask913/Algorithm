from collections import deque
import copy
n,m = map(int,input().split())
office = []
dx,dy = [0,0,1,-1],[-1,1,0,0] # 왼 오 하 상
dic = {
    1:[[0],[1],[2],[3]],
    2:[[0,1],[2,3]],
    3:[[0,2],[0,3],[1,2],[1,3]],
    4:[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    5:[[0,1,2,3]]
}
"""
0은 빈 칸, 6은 벽, 1
1 -> 상/하/좌/우 
2 -> 상,하/좌,우
3 -> 상,오 / 오,하 / 하,왼/왼,상
4 -> 상,하,좌/상,하,우/좌,우,상/좌,우,하
5 -> 상,하,좌,우
"""
for _ in range(n):
    office.append(list(map(int,input().split())))

def cctv(tx,ty,d,tmp):
    for i in d:
        x,y = tx,ty
        while True:
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny] != 6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
                x,y = nx,ny
            else:
                break

res = []
def blind_spot(r):
    global res
    cnt = 0
    for i in r:
        for j in i:
            if j == 0:
                cnt += 1
    res.append(cnt)

def bruteforce(seq,q,r):
    if len(q)<=seq:
        blind_spot(r)
        return

    for k in range(seq,len(q)):
        x,y,c = q[k]
        for i in dic[c]:
            temp = copy.deepcopy(r)
            cctv(x,y,i,temp)
            bruteforce(k+1,q,temp)

q = deque()
for i in range(n):
    for j in range(m):
        if 0<office[i][j]<6:
            q.append((i,j,office[i][j]))

t = copy.deepcopy(office)
bruteforce(0,q,t)

print(min(res))