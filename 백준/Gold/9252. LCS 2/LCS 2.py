""" LCS 공통 부분 수열 """
a = input()
b = input()
n,m = len(a),len(b)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

x,y = n,m
ans = ''
while x > 0 and y > 0: # 현재 좌표 (x,y) 위 아래에 동일한 값을 가지지 않는 좌표 탐색
    if dp[x-1][y] == dp[x][y]:
        x -= 1
    elif dp[x][y-1] == dp[x][y]:
         y -= 1
    else:
        ans += a[x-1]
        x -= 1
        y -= 1

print(dp[n][m])
print(ans[::-1])