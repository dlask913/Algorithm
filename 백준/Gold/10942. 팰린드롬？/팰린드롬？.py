import sys
input = sys.stdin.readline
n = int(input())
dp=[[0 if i!=j else 1 for i in range(j+1)] for j in range(n)]
lst = list(map(int,input().split()))
m = int(input())

for i in range(n):
    for j in range(i+1):
        if i<(n-1) and lst[i] == lst[i+1]:
            dp[i+1][i]=1
        if (i-1)>=0 and (j+1)<i and dp[i-1][j+1] and lst[i]==lst[j]:
            dp[i][j]=1

for _ in range(m):
    s,e=map(int,input().split())
    print(dp[e-1][s-1])
