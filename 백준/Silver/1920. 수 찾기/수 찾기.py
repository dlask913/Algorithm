import sys
n= int(sys.stdin.readline())
a= list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b= list(map(int,sys.stdin.readline().split()))

a.sort()

def binary_search(a,n,l,k,r):
    if l > r:
        print(0)
        return
    if a[k] > n:
        binary_search(a,n,l,(l+k-1)//2,k-1)
    elif a[k] < n:
        binary_search(a, n, k+1, (k+1 + r) // 2, r)
    else:
        print(1)
        return 


for i in b:
    binary_search(a,i,0,(n-1)//2,n-1)