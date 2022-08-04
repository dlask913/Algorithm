dw = [-1,0,1,-1,1,-1,0,1] # j
dh = [-1,-1,-1,0,0,1,1,1] # i
def search(dh,dw,queue,visited,graph,cnt):
    while queue:
        x, y = queue.pop(0)
        for i,j in zip(dh,dw):
            try:
                if (i < 0 and x<=0) or (j<0 and y<=0):
                    pass
                elif visited[x+i][y+j]==0 and graph[x+i][y+j]==1:
                    visited[x+i][y+j]=cnt
                    queue.append((x+i,y+j))
            except IndexError:
                pass
while True:
    w,h = map(int,input().split())
    visited = [[0 for _ in range(w)] for _ in range(h)]
    queue = []
    cnt = 0
    if w==0 and h==0:
        break

    graph=[]
    for i in range(h):
        graph.append(list(map(int,input().split())))
    cnt = 1
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==0:
                visited[i][j] =cnt
                queue.append((i,j))
                search(dh,dw,queue,visited,graph,cnt)
                cnt += 1
    print(cnt-1)