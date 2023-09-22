def solution(n, m):
    x,y = n, m
    while y > 0: # 유클리드
        x,y = y,x%y
        
    return [x,(n*m)//x]