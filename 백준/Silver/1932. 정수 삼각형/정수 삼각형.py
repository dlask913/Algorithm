n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))
    temp = [0]*(n-i-1)
    dp[i] += temp

for i in range(1,n):
    for j in range(i+1):
        dp[i][j] += max(dp[i-1][j],dp[i-1][j-1])
print(max(dp[n-1]))
      