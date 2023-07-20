def solution(maps):
    x_len,y_len = len(maps),len(maps[0])
    v = [[0 for _ in range(y_len)] for _ in range(x_len)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer = []
    
    for i in range(x_len):
        for j in range(y_len):
            if maps[i][j] != 'X' and v[i][j] ==0:
                v[i][j] = 1
                q = [(i,j)]
                s = int(maps[i][j])
                while q:
                    x,y = q.pop()
                    for k in range(4):
                        nx,ny= dx[k]+x,dy[k]+y
                        if 0<=nx<x_len and 0<=ny<y_len and v[nx][ny]==0 and maps[nx][ny] != 'X':
                            v[nx][ny] =1
                            q.append((nx,ny))
                            s += int(maps[nx][ny])
                answer.append(s)
    if not answer: return [-1]
    answer.sort()
    return answer