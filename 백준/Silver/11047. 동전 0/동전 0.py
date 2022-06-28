n, k = map(int,input().split())
A = list()
cnt = 0
for i in range(n):
    a = int(input())
    A.append(a)
A.sort(reverse=True)
for j in range(len(A)):
    if A[j] <= k:
        cnt += k//A[j]
        k = k % A[j]
print(cnt)