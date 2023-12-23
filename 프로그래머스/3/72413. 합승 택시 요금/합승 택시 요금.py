import heapq

def dijkstra(graph,start,d):
    hq = []
    heapq.heappush(hq,[0,start])
    dist = [float('inf') for _ in range(len(graph)+1)]
    dist[start] = 0
    
    while hq:
        cost, node = heapq.heappop(hq) # 현재 비용, 현재 노드
        if cost > dist[node]:
            # 현재 계산한 요금보다 더할 요금이 더 크면 pass
            continue
        
        for c,n in graph[node]:
            tmp = cost + c # 현재 요금 + n(이어진 노드)까지 가는 요금
            if dist[n] > tmp:
                dist[n] = tmp
                heapq.heappush(hq,(tmp,n))
                
    return dist[d] # 도착지 최소 경로 비용

def solution(n, s, a, b, fares): # s=출발지
    answer = 0
    graph = {i:[] for i in range(1,n+1)}
    for x,y,c in fares:
        graph[x].append((c,y))
        graph[y].append((c,x))
        
    # 구간 별 최소 경로 구하기→ 출발지~중간지점 + 중간지점~a도착지 + 중간지점~b도착지
    res = 10000*200
    for k in range(1,n+1):
        res = min(res,dijkstra(graph,s,k)+dijkstra(graph,k,a)+dijkstra(graph,k,b))
        
    return res