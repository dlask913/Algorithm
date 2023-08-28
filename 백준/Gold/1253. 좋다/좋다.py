n = int(input())
A = list(map(int,input().split()))
A.sort()
ans = 0

for k,v in enumerate(A):
    l = 0
    r = n-1
    while l < r:
        if l == k:
            l = k+1
            continue
        elif r == k:
            r = k-1
            continue

        if (A[l]+A[r]) > v:
            r -= 1
        elif (A[l]+A[r]) < v:
            l += 1
        else:
            ans += 1
            break

print(ans)