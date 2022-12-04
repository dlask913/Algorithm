import math
INF = math.inf
n,m = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)

left = 0
right = left + 1
min_ = INF
while left < n and right < n:
    temp = abs(lst[left]-lst[right])
    if temp > m:
        min_ = min(temp,min_)
        left += 1
    elif temp == m:
        min_ = min(temp, min_)
        right += 1
    else:
        right += 1


print(min_)