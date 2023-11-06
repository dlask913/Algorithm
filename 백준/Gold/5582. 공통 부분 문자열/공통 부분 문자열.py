""" Longest Common Substring(최장 공통 문자열) , 부분 수열이 아니라는 점에서 흔히 알고 있는 LCS와 차이가 있음"""
a = input()
b = input()
n,m = len(a),len(b)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
res = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            res = max(dp[i][j], res)

print(res)