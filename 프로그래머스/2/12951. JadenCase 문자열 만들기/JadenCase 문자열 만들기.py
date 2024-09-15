def solution(s):
    answer = list(s.lower())
    
    for x in range(len(answer)):
        if (x == 0 or answer[x-1] == ' ') and answer[x].isalpha():
            answer[x] = answer[x].upper()
    
    return ''.join(answer)