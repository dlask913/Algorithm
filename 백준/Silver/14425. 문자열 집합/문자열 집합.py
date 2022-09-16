n,m=map(int,input().split())
a=[]
b=[]
cnt = 0
for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())
a.sort()
def binary_search(st,l,r):
    global cnt
    if l>r:
        return
    k=(l+r)//2
    if a[k]>st:
        binary_search(st,l,k-1)
    elif a[k]<st:
        binary_search(st,k+1,r)
    else:
        cnt += 1

for i in b:
    binary_search(i,0,n-1)

print(cnt)