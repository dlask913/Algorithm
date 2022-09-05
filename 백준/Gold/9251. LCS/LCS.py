st = input()
st2 = input()
dp=[[0 for _ in range(1002)] for _ in range(1002)]
for i in range(1,len(st)+1):
    flag = True
    for j in range(1,len(st2)+1):
        if st[i-1]==st2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

max_ = 0
for i in dp:
    if max_ < max(i):
        max_ = max(i)
print(max_)