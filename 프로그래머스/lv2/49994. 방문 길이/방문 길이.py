def solution(dirs):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    dic = {"U":0,"D":1,"R":2,"L":3}
    q = []
    x,y = 0,0
    
    for i in dirs:
        d = dic[i]
        nx,ny = x+dx[d],y+dy[d]
        if -5<=nx<=5 and -5<=ny<=5:
            q.append((x,y,nx,ny))
            q.append((nx,ny,x,y))
            x,y = nx,ny
            
    answer = len(set(q))//2
    return answer