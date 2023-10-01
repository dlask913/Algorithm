""" dp
k는 행, n은 열로 dp[k][n] 은 k개의 숫자 합으로 n 을 만들 수 있는 조합의 개수
ex> k=2, n=4 일 때.. (0,4) (1,3) (2,2) (3,1) (4,0) 으로 dp[k][n] = 5
점화식 은 dp[k][n] = dp[k-1][0] + dp[k-1][1] + dp[k-1][2] + .. + dp[k-1][n]
idx     0 1 2 3 4 (n)
1(k)    1 1 1 1 1
2(k)    1 2 3 4 5
에서 dp[k][n] 는 사실상 dp[k-1][n] + dp[k][n-1] 임을 알 수 있다.
"""

n, k = map(int,input().split())
dp = [[1 if x == 0 or y == 1 else 0 for x in range(n+1)] for y in range(k+1)]

for i in range(2,k+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] # 점화식

print(dp[k][n] % 1000000000)