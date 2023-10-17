n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
dp = [[0 if i!=0 else -3276800 for _ in range(m+1)] for i in range(n+1)]
s = [0 for _ in range(n+1)]

for i in range(1,n+1):
    s[i] = s[i-1] + arr[i-1]
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i - 1][j];
        if j==1:
            dp[i][j] = max(dp[i][j], s[i])
        for k in range(2,i+1):
            dp[i][j] = max(dp[i][j], dp[k - 2][j - 1] + s[i] - s[k - 1]);

print(dp[n][m])