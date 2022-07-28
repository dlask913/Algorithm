n,m,v=map(int,input().split())
graph= {i:[] for i in range(n+1)}
visited=[0 for _ in range(n+1)]

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
            print(i,end=' ')
            dfs(i,graph,visited)
print(v,end=' ')
visited[v]=1
dfs(v,graph,visited)

queue=[]
queue.append(v)
visited=[0 for _ in range(n+1)]
visited[v]=1

def bfs(v,graph,visited,q):
    for i in graph[v]:
        if visited[i]==0:
            q.append(i)
            visited[i]=1
    if q:
        v=q.pop(0)
        print(v,end=' ')
        bfs(v,graph,visited,q)
    else:
        return
print()
bfs(v,graph,visited,queue)

