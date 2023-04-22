import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
stack = []
res = [-1 for _ in range(n)]

stack.append(0)
for i in range(1,n):
    if A[i] > A[stack[-1]]:
        while stack and A[stack[-1]] < A[i]:
            idx = stack[-1]
            if A[idx] < A[i]:
                stack.pop()
                res[idx] = A[i]
    stack.append(i)

for i in res:
    print(i,end=' ')