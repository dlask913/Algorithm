def solution(wallpaper):
    lx,ly = len(wallpaper),len(wallpaper[0])
    x1,y1,x2,y2= lx,ly,0,0

    for i in range(lx):
        for j in range(ly):
            if wallpaper[i][j] == '#':
                x1 = min(x1,i)
                y1 = min(y1,j)
                x2 = max(x2,i+1)
                y2 = max(y2,j+1)
                
    return [x1,y1,x2,y2]