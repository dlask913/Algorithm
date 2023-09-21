def solution(price, money, count):
    ans = money - sum([price*i for i in range(1,count+1)])
    return 0 if ans>0 else abs(ans)