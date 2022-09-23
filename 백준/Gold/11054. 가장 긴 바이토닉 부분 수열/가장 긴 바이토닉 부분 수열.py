n=int(input())
a=list(map(int,input().split()))
dp=[1 for _ in range(n)]
k=[1 for _ in range(n)]

for i in range(n):
    for j in range(i - 1, -1, -1):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    for j in range(n-i-1,n):
        if a[n-i-1] > a[j]:
            k[n-i-1] = max(k[n-i-1], k[j] + 1)

max_=1
for i,j in zip(dp,k):
    max_ = max(max_,i+j)
print(max_-1)