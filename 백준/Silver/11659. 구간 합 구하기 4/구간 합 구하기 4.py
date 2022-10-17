import sys
input = sys.stdin.readline
n,m=map(int,input().split())
num = list(map(int,input().split()))
sum_=[0]
temp =0
for i in num:
    temp += i
    sum_.append(temp)

for _ in range(m):
    x,y = map(int,input().split())
    print(sum_[y]-sum_[x-1])