n,k = map(int,input().split())
sum_ = 0

for i in range(1,k+1):
    sum_ += i

if sum_ > n:
    print(-1)
elif (n-sum_) % k == 0:
    print(k-1)
else:
    print(k)
