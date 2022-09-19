import sys
n= int(sys.stdin.readline())
liq=list(map(int,sys.stdin.readline().split()))
liq.sort()
left = 0
right = n-1
min_ = [1000000001,1000000001]
while left < right:
    temp = [liq[left],liq[right]]
    min_ = temp if abs(sum(min_)) > abs(sum(temp)) else min_
    if abs(liq[left])<abs(liq[right]):
        right -=1
    else:
        left += 1
print(min_[0],min_[1])