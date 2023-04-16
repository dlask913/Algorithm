import sys
input = sys.stdin.readline
v = int(input())
graph = {x:[] for x in range(1,v+1)}
ans = []

def list_chunk(lst, n): # n씩 리스트 자르기
    return [lst[i:i+n] for i in range(0, len(lst), n)]

for x in range(v):
    tmp = list(map(int,input().split()))
    seq = tmp[0]
    tmp = list_chunk(tmp[1:-1],2)
    for i in tmp:
        graph[seq].append(i)
    graph[seq].sort(key=lambda x:-x[1])

def dfs(start,cost,visited):
    for i in graph[start]:
        if visited[i[0]] == 0:
            visited[i[0]] = cost+i[1]
            dfs(i[0],visited[i[0]],visited)


visited = [0 for _ in range(v+1)]
dfs(1,0,visited)
idx = visited.index(max(visited))
visited = [0 for _ in range(v+1)]
dfs(idx,0,visited)
visited[idx] = 0
print(max(visited))