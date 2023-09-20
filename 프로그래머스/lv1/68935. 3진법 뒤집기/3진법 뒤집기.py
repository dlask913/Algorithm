def solution(n):
    answer = 0
    st = ''
    while n > 0:
        st+=str(n%3)
        n //= 3

    for i in range(len(st)):
        answer += int(st[i])*3**(len(st)-i-1)
        
    return answer