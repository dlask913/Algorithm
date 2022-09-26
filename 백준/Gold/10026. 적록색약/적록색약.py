n = int(input())
graph = []
dx=[0,0,1,-1]
dy=[1,-1,0,0]
rg_v = [[0 for _ in range(n)] for _ in range(n)]
q=[]
rg_cnt=cnt=0

for _ in range(n):
    graph.append(list(input()))

def bfs(q,color):
    while q:
        x, y = q.pop()
        for i, j in zip(dx, dy):
            if 0<=(x+i)<n and 0<=(y+j)<n and graph[x+i][y+j] == color and v[x+i][y+j] == 0:
                v[x+i][y+j] = 1
                q.append((x+i,y+j))

def rg_bfs(q,color):
    while q:
        x, y = q.pop()
        for i, j in zip(dx, dy):
            if color =='B':
                if 0<=(x+i)<n and 0<=(y+j)<n and graph[x+i][y+j] == color and v[x+i][y+j] == 0:
                    v[x+i][y+j] = 1
                    q.append((x+i,y+j))
            else:
                if 0<=(x+i)<n and 0<=(y+j)<n and graph[x+i][y+j] != 'B' and v[x+i][y+j] == 0:
                    v[x+i][y+j] = 1
                    q.append((x+i,y+j))

v = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            q.append((i,j))
            bfs(q,graph[i][j])
            cnt+=1

v = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            q.append((i, j))
            rg_bfs(q, graph[i][j])
            rg_cnt += 1
print(cnt,rg_cnt)