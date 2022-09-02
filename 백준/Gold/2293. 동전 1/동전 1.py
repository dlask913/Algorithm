n,k=map(int,input().split())
v=[0]
dp=[0 for _ in range(k+1)]
for _ in range(n):
    v.append(int(input()))
v.sort()
for i in range(1,n+1):
    for j in range(1,k+1):
        if v[i]>j:
            continue
        if v[i] == j:
            dp[j]+=1
        dp[j]=dp[j]+dp[j-v[i]]
print(dp[-1])