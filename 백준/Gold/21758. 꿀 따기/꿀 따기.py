n = int(input())
bee = list(map(int,input().split()))
sum_ = [0 for _ in range(n)]
sum_[0] = bee[0]
for i in range(1,n):
    sum_[i] = sum_[i-1]+bee[i]
honey=0
for i in range(1,n-1):
    honey=max(honey,sum_[i]-bee[0]+sum_[n-2]-sum_[i-1])
    honey = max(honey, sum_[n - 2] - bee[i] + sum_[i - 1])
    honey=max(honey,sum_[n-1]-bee[0]-bee[i]+sum_[n-1]-sum_[i])
print(honey)