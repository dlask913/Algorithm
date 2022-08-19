n  = int(input())
grape =[0 for _ in range(10003)]
dp = [0 for _ in range(10003)]
for i in range(n):
    grape[i]=int(input())

dp[0] = grape[0]
dp[1] = grape[0]+grape[1]
dp[2] = max(grape[0]+grape[2],grape[1]+grape[2],dp[1])

for i in range(3,n+1):
    dp[i]= max(dp[i-3]+grape[i-1]+grape[i],dp[i-2]+grape[i],dp[i-1])

if n<3:
    print(sum(grape))
else:
    print(dp[n])