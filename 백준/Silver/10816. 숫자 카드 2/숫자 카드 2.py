import sys
from bisect import bisect_left, bisect_right
n= int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
cnt=[0 for _ in range(m)]
a.sort()

def binary_search(a,l,r):
    right = bisect_right(a,r)
    left = bisect_left(a,l)
    return right-left

for i in b:
    print(binary_search(a,i,i),end=' ')
