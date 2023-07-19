from collections import deque
def solution(n, edge):
    INF = int(1e9)
    graph = {i:[] for i in range(1,n+1)}
    v = [INF for _ in range(n+1)]
    v[0],v[1] = 0,0
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    q = deque([(1,0)])
    
    while q:
        x,c = q.popleft()
        for i in graph[x]:
            if v[i] == INF:
                v[i] = c+1
                q.append((i,v[i]))
    answer = v.count(max(v))
    return answer