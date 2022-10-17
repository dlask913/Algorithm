import math
n=int(input())
a,b=map(int,input().split())
graph={i+1:[] for i in range(n+1)}
m=int(input())
v=[0 for i in range(n+1)]
res = math.inf
for _ in range(m):
    x,y =map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start,cnt):
    global res
    if start==b:
        res = cnt if cnt<res else res
        return
    v[start]=1
    for i in graph[start]:
        if v[i]==0:
            v[i]=1
            dfs(i,cnt+1)
            v[i]=0
dfs(a,0)
if res==math.inf:
    print(-1)
else:
    print(res)