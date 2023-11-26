def solution(s, n):
    answer = ''
    for x in s:
        c = ' '
        if x != ' ':
            c = chr(ord(x) + n)
            
        if x.isupper() and ord(c) > 90:
            c = chr(ord(c)%90+64)
        
        if x.islower() and ord(c) > 122:
            c = chr(ord(c)%122+96)
        
        answer += c
        
    return answer