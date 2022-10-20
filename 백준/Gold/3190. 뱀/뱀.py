from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
graph=[[0 for _ in range(n)] for _ in range(n)]
dx=[0,0,1,-1] # 오, 왼, 아, 위
dy=[1,-1,0,0]
d=[]
for _ in range(k):
    x,y=map(int,input().split())
    graph[x-1][y-1]='A'
l = int(input())
for _ in range(l):
    x,c=input().split()
    d.append((int(x),c))

def direct_change():
    global lev
    if lev == 0:
        return 0
    elif lev == 1:
        return 2
    elif lev == 2:
        return 1
    elif lev == 3:
        return 3
    elif lev > 3:
        lev = 0
        return 0
    elif lev < 0:
        lev = 3
        return 3

sec = 0
x,y,nx,ny = 0,0,0,1
lev = 0
q=deque()
q.append((x,y))

while True:
    if not (0<=x<n and 0<=y<n):
        break
    if ( x != 0 or y != 0 ) and (x,y) in q:
        break
    q.append((x,y))
    if graph[x][y]=='A':
        graph[x][y]=2
    else:
        graph[x][y]=1
        q.popleft()
    if d and sec == d[0][0]:
        if d[0][1] == 'D':   lev += 1
        elif d[0][1] == 'L': lev -= 1
        temp = direct_change()
        nx = dx[temp]
        ny = dy[temp]
        d.pop(0)
    x += nx
    y += ny
    sec += 1
print(sec)
