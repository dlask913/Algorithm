def solution(n):
    answer = 0
    cnt = bin(n).count('1')
    nex = n+1
    
    while True:
        if cnt == bin(nex).count('1'):
            answer = nex
            break       
        nex += 1
        
    return answer