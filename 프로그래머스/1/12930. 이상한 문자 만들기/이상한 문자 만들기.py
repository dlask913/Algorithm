def solution(s):
    answer = ''
    for x in s.split(" "):
        for k,v in enumerate(x):
            if k%2==0:
                answer += v.upper()
            else:
                answer += v.lower()
        answer += ' '
        
    return answer[:-1]