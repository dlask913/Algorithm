""" LCS 공통 부분 수열 - 3차원 
문자열 A,B,C 가 주어졌을 때 LCS(LCS(A,B),C) 를 하게 되면 X
A와 B의 LCS가 C를 포함하였을 때 동일할 지가 보장되지 X
"""
a = input()
b = input()
c = input()
dp = [[[0 for _ in range(len(c)+1)] for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        for k in range(1,len(c)+1):
            if a[i-1] == b[j-1] == c[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

print(dp[len(a)][len(b)][len(c)])