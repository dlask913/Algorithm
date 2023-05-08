def directions(d):
    if d=="E": return 0
    elif d=="W": return 1
    elif d=="N": return 3
    else: return 2
    
def solution(park, routes):
    answer = []
    # 동, 서, 남, 북
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    x,y=0,0
    l = len(park[0])
    for i in range(len(park)):
        for j in range(l):
            if park[i][j]=="S":
                x,y=i,j
                break
    
    for i in routes:
        d,step = i.split()
        step=int(step)
        d = directions(d)
        nx,ny = x,y
        flag = True
        for j in range(step):
            nx += dx[d]
            ny += dy[d]
            if 0>nx or nx>=len(park) or 0>ny or ny>=l or park[nx][ny]=="X":
                flag = False
                break
            
        if flag:
            x,y=nx,ny
            answer=[nx,ny]
    if not answer:
        return [x,y]
    return answer