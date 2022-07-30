t = int(input())
graph = []
visited = []
queue= []
def search(graph,visited, queue,n,m):

    while queue:
        x, y = queue.pop(0)

        if x < (n-1) and graph[x+1][y]==1 and visited[x+1][y]==0:
            visited[x+1][y] = 1
            queue.append((x+1,y))
        if y < (m-1) and graph[x][y+1]==1 and visited[x][y+1]==0:
            visited[x][y+1] = 1
            queue.append((x,y+1))
        if x > 0 and graph[x-1][y]==1 and visited[x-1][y]==0:
            visited[x-1][y] = 1
            queue.append((x-1,y))
        if y > 0 and graph[x][y-1] == 1 and visited[x][y-1] == 0:
            visited[x][y-1] = 1
            queue.append((x, y-1))


for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[ 0 for _ in range(m)] for _ in range(n)]
    visited = [[ 0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for j in range(k):
        x,y = map(int,input().split())
        graph[y][x]=1
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1 and visited[a][b]==0:
                queue.append((a,b))
                search(graph,visited,queue,n,m)
                cnt += 1
    print(cnt)
