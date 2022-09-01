import sys
n,k=map(int,sys.stdin.readline().split())
backpack=[]
dp=[0 for _ in range(k+1)]
for i in range(n):
    w,v=map(int,sys.stdin.readline().split())
    backpack.append((w,v))

for i in range(n):
    w,v = backpack.pop()
    for j in range(k,w-1,-1):
        if w > j:
            continue
        dp[j] = max(dp[j-w]+v,dp[j])
print(dp[-1])