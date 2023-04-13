n = int(input())
T = [[0,0]]
P = [0]
dp = [0 for _ in range(n+1)]
for i in range(n):
    t,p = map(int,input().split())
    T.append([i+1,i+t])
    P.append(p)

for i in range(1,n+1): # i가 현재,T[i][0]이 i의 시작일,T[i][1]가 해당 i의 종료일, P[i]가 비용
    for j in T:
        if j[1] == i: # 현재 종료인 T가 있는지
            dp[i] = max(dp[j[0]-1]+P[j[0]],dp[i])
        else:
            dp[i] = max(dp[i],dp[i-1])
print(dp[n])