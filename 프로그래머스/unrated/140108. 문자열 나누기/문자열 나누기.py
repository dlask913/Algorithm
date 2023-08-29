def solution(s):
    answer = 1
    x = s[0]
    cnt = 1
    for i in range(1,len(s)):
        if cnt == 0:
            answer += 1
            x = s[i]
        if s[i] == x:
            cnt += 1
        else: 
            cnt -= 1
            
    return answer