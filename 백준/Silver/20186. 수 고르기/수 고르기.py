import sys
n,k=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
res=0
for i in range(1,k+1):
    res+=lst[-i]-i+1
print(res)