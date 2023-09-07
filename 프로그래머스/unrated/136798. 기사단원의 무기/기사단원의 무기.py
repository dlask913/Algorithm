def divisor(n):
    cnt = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            cnt += 1
            if i**2 != n:
                cnt += 1
    return cnt    
        
def solution(number, limit, power):
    answer = 1
    
    for i in range(2,number+1):
        att = divisor(i)
        if att > limit:
            att = power
        answer += att
    
    return answer