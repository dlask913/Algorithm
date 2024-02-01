t = int(input())

def manhattan(x1,x2,y1,y2):
    return abs(x1-x2)+abs(y1-y2)

def bfs(loc,s,e): # 편의점 개수, 편의점 좌표, 출발지(집), 도착지(페스티벌)
    q = [(s[0],s[1])]
    while q:
        x, y = q.pop(0) # 현재 위치
        if x == e[0] and y == e[1]:
            return "happy"
        for _ in range(len(loc)):
            cx,cy = loc.pop(0)
            if 0 < manhattan(x,cx,y,cy) <= 1000: # 현재 맥주 개수로 갈 수 있다면,
                q.append((cx,cy))
            else:
                loc.append((cx,cy))
    return "sad"

for _ in range(t):
    n = int(input())
    home = list(map(int,input().split())) # 출발지
    coordinate = [] #  n개의 편의점 좌표
    for _ in range(n+1):
        x,y = map(int,input().split())
        coordinate.append((x,y)) # (편의점 x, 편의점 y)
    print(bfs(coordinate,home,coordinate[-1])) # 편의점 좌표, 출발지, 도착지
