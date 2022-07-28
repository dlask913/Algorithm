n = int(input())
m = int(input())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
visited[1]=1
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(idx,graph,visited):
    for i in graph[idx]:
        if visited[i]==0:
            visited[i]=1
            dfs(i,graph,visited)

dfs(1,graph,visited)
print(visited.count(1)-1)