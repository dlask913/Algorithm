n = int(input())
tmp = list(map(int, input().split()))
h = [(k,v) for k,v in enumerate(tmp)]
res = []

def check(m,point1,point2):
    if point1>point2:
        point1,point2=point2,point1
    for x in range(point1+1,point2):
        if h[x][1] >= m*(h[x][0]-h[point1][0])+h[point1][1]: # 방정식 아래 영역을 벗어난다면
            return False
    return True


for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if j == i+1 or j == i-1:
            cnt += 1
            continue
        m = (h[j][1]-h[i][1])/(h[j][0]-h[i][0]) # 기울기
        if check(m, i, j):
            cnt += 1
    res.append(cnt)

print(max(res))