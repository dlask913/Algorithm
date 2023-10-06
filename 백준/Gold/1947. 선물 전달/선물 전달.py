# DP 완전 순열 문제 ( 자기 모자 안 쓰는 경우의 수 )
n = int(input())
dp = [0 for _ in range(n)]
if n > 1:
    dp[1] = 1
for i in range(2, n):
    dp[i] = (i*(dp[i-1]+dp[i-2])) % 1000000000 # 완전 순열 점화식
print(dp[n-1])
