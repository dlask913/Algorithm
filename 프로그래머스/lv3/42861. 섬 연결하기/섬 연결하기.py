import heapq
# PRIM 
def solution(n, costs):
    answer = 0
    graph = {i:[] for i in range(n)}
    v = [0 for _ in range(n)]
    for i,j,k in costs:
        graph[i].append((k,j))
        graph[j].append((k,i))
        
    q = [(0,0)]  
    while q:
        c,x = heapq.heappop(q)
        if not v[x]:
            v[x] = 1
            answer += c
            for i in graph[x]:
                if v[i[1]] == 0:
                    heapq.heappush(q,(i[0],i[1]))
    
    return answer