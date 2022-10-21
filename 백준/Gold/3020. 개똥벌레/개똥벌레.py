import sys
input=sys.stdin.readline
n,h=map(int,input().split())
low = [0]*h
high = [0]*h
cave = [0]*h
for i in range(n):
    if i%2 == 0:
        low[int(input())-1]+= 1
    else:
        high[int(input())-1]+=1

for i in range(h-1,0,-1):
    low[i-1] +=low[i]
    high[i-1]+= high[i]

for i in range(h):
    cave[i] = low[i]+high[h-(i+1)]

print(min(cave),cave.count(min(cave)))