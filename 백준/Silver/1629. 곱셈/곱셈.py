import sys
input = sys.stdin.readline
a,b,mod=map(int,input().split())

def power(C, n):
    if n == 0:
        return 1
    if n == 1:
        return C

    x = power(C, n//2)
    if n % 2 == 0:
        return x * x % mod
    else:
        return x * x * C % mod

print(power(a,b) % mod)
