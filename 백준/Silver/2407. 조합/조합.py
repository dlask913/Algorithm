n,k=map(int,input().split())

def fact(x):
    if x==1: return 1
    return fact(x-1)*x

print(fact(n)//(fact(k)*fact(n-k)))