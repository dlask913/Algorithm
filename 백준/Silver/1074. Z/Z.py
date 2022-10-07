import sys
n,r,c = map(int,sys.stdin.readline().split())

num=0
k = 2**n
while True:
    if k<=1: break
    k//=2
    if r<k and c<k: continue
    elif r<k and c>=k:
        c-=k
        num += k**2
    elif r>=k and c<k:
        r-=k
        num += (k**2)*2
    elif r>=k and c>=k:
        r-=k
        c-=k
        num += (k**2)*3

print(num)