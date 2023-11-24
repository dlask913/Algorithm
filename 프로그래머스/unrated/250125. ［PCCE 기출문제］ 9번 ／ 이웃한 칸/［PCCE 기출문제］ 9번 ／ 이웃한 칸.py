def solution(board, h, w):
    answer = 0
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    
    for i in range(4):
        nx,ny = dx[i]+h,dy[i]+w
        if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[h][w] == board[nx][ny]:
            answer += 1
    
    return answer