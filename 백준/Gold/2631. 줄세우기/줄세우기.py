# 최장 증가 부분 수열(LIS, Longest Increasing Subsequence) → DP
n = int(input())
line = []
dp = [1 for _ in range(n)]
for _ in range(n):
    line.append(int(input()))

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if line[i] > line[j]:
            dp[i] = max(dp[i],dp[j]+1) 
            
print(n-max(dp))