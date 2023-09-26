from collections import deque
T = int(input())
def dag(v,d): # 위상 정렬
    q = deque()
    dp = [0 for _ in range(len(v))] # 최대값 갱신
    for i in range(len(v)):
        if v[i] == 0: # 진입 차수 0
            q.append(i)
            dp[i] = d[i]

    while q:
        x = q.popleft()
        for i in dic[x]:
            v[i] -= 1
            dp[i] = max(dp[i], dp[x] + d[i])
            if v[i] == 0:
                q.append(i)
    return dp

for _ in range(T):
    n,k = map(int,input().split())
    d = list(map(int,input().split()))
    dic = {i:[] for i in range(n)}
    v = [0 for _ in range(n)] # 진입 차수 저장
    for _ in range(k):
        x,y = map(int,input().split())
        dic[x-1].append(y-1)
        v[y-1] += 1
    w = int(input())-1
    res = dag(v,d)
    print(res[w])
