from collections import deque

n,m = map(int,input().split())
board = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
dq = deque()
cnt,rem = 0,-1
for _ in range(n):
    board.append(list(map(int,input().split())))

def check(graph,cost):
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                cost += 1
    return cost

def cheese(dq):
    v = [[0 for _ in range(m)] for _ in range(n)]
    global cnt
    dq.append((0,0))
    rem = check(board,0)
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx ,ny = dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<m and v[nx][ny]==0:
                v[nx][ny] = 1
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                elif board[nx][ny] == 0:
                    dq.append((nx,ny))
    cnt += 1

    if check(board,0) != 0:
        cheese(dq)
    else:
        print(cnt)
        print(rem)
        return

cheese(dq)