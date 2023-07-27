from collections import deque
def bfs(maps,i,j,point):
    global ans
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    xlen,ylen = len(maps),len(maps[0])
    v = [[0 for _ in range(ylen)] for _ in range(xlen)]
    q = deque([(i,j)])
    cnt = 1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny = dx[i]+x,dy[i]+y
                if 0<=nx<xlen and 0<=ny<ylen and maps[nx][ny]!='X' and v[nx][ny] == 0:
                    if maps[nx][ny] == point:
                        return cnt
                    q.append((nx,ny))
                    v[nx][ny] = 1
        cnt += 1
    return -1

def solution(maps):
    lever,end = 0,0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                lever = bfs(maps,i,j,'L')
            if maps[i][j] == 'L':
                end = bfs(maps,i,j,'E')
    
    return (lever + end) if lever>0 and end>0 else -1