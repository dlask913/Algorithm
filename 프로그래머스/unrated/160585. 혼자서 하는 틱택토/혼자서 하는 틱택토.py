def check(board,x):
    flag = False
    for i in range(3):
        if board[0][i] == x and board[1][i] == x and board[2][i] == x: #세로
            flag = True
        if board[i][0] == x and board[i][1] == x and board[i][2] == x: #가로
            flag = True
    if board[0][0] == x and board[1][1] == x and board[2][2] == x: #대각선
        flag = True
    if board[0][2] == x and board[1][1] == x and board[2][0] == x: #대각선
        flag = True
        
    return flag
    
def solution(board):
    st = ''.join(board)
    o = st.count('O')
    x = st.count('X')
    
    if x>o or o>(x+1):
        return 0
    elif check(board,'O') and o != (x+1): # O가 이김-> o = x+1
        return 0
    elif check(board,'X') and o != x: # X가 이김-> x = o
        return 0
    
    return 1