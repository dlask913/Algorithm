def solution(dirs):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    dic = {"U":0,"D":1,"R":2,"L":3}
    answer = 0
    q = []
    x,y = 5,5
    
    for i in dirs:
        d = dic[i]
        nx,ny = x+dx[d],y+dy[d]
        if 0<=nx<=10 and 0<=ny<=10:
            q.append((x,y,nx,ny))
            q.append((nx,ny,x,y))
            x,y = nx,ny
            
    answer = len(set(q))//2
    return answer