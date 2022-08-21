n,m=map(int,input().split())
graph= {i:[] for i in range(n+1)}
visited=[0 for _ in range(n+1)]
cnt =0
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[x].sort()
    graph[y].append(x)
    graph[y].sort()

def dfs(v,graph,visited):
    for i in graph[v]:
        if visited[i]==0:
            visited[i]=1
            dfs(i,graph,visited)

for i in range(1,n+1):
    if visited[i] ==0:
        dfs(i,graph,visited)
        cnt += 1
print(cnt)