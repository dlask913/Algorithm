""" 플로이드-워셜 """

import math,copy
inf = math.inf
n,K = map(int,input().split()) # 개수, 위치
v = 0 # 비트마스킹을 통한 방문 처리
T = [] # T(i,j) 는 i부터 j 행성 까지 걸리는 시간
d = [[inf for _ in range(n)] for _ in range(n)] # 최소 거리 갱신
ans = inf
for _ in range(n):
    T.append(list(map(int,input().split())))
d = copy.deepcopy(T) # 초기 비용
v |= (1 << K)

def dfs(visit,s,cost): # (방문 체크,거리,비용)
    global ans
    if visit == (1 << n)-1:
        ans = min(ans,cost)
        return

    for i in range(n):
        if i != s and not visit & (1 << i):
            visit |= (1 << i) # 방문 처리
            dfs(visit,i,cost+d[s][i])
            visit &= ~(1 << i) # 방문 취소

for i in range(n):
    for j in range(n):
        for k in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]) # 플로이드 워셜 점화식

dfs(v,K,0)
print(ans)