n,s = map(int,input().split())
a = list(map(int,input().split()))
sum_ = [0]
temp = 0
for i in a:
    temp += i
    sum_.append(temp)
start = 0
end = 1
res = []
while True:
    if end > n:
        break
    if sum_[end]-sum_[start] < s:
        end += 1
    else:
        res.append(end-start)
        start += 1
if not res:
    print(0)
else:
    print(min(res))