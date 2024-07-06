def solution(s):
    answer = ''
    l = len(s)//2
    if len(s) % 2 == 0:
        answer = s[l-1]+s[l]
    else:
        answer = s[l]
    return answer