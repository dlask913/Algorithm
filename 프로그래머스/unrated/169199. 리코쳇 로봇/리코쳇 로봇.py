res = []
def dfs(board,x,y,v,cnt):
    global res
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    lx,ly = len(board),len(board[0])
    v[x][y] = cnt
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<lx and 0<=ny<ly:
            while True:
                if (0>nx or 0>ny or lx<=nx or ly<=ny) or (0<=nx<lx and 0<=ny<ly and board[nx][ny] == 'D'):
                    if board[nx-dx[i]][ny-dy[i]] == 'G':
                        res.append(cnt)
                        return
                    if v[nx-dx[i]][ny-dy[i]]==0 or v[nx-dx[i]][ny-dy[i]] > (cnt+1):
                        dfs(board,nx-dx[i],ny-dy[i],v,cnt+1)
                    break
                nx,ny = nx+dx[i],ny+dy[i]    

def solution(board):
    lx,ly = len(board),len(board[0])
    v = [[0 for _ in range(ly)] for _ in range(lx)]
    for i in range(lx):
        for j in range(ly):
            if board[i][j] == 'R':
                dfs(board,i,j,v,1)
                break
    if not res: return -1
    return min(res)