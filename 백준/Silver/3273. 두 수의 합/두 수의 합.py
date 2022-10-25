n=int(input())
lst = list(map(int,input().split()))
x=int(input())
lst.sort()
start = 0
end = n-1
cnt = 0
while start<end:
    if start<0 or end >=n:
        break
    if (lst[start]+lst[end]) == x:
        cnt += 1
    if (lst[start]+lst[end]) <= x:
        start += 1
    else:
        end -= 1

print(cnt)
