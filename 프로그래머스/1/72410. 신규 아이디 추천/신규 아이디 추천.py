def solution(new_id):
    answer = ''
    
    symbols = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = new_id.lower()
    for x in symbols:
        new_id = new_id.replace(x,'')
        
    for x in new_id.split('.'):
        if x:
            answer += (x+'.')
    answer = answer.strip('.')
    
    if not answer:
        answer = 'aaa'
    elif len(answer) >= 16:
        answer = answer[:15]
    elif len(answer) <= 2:
        answer += (answer[-1]*(3-len(answer)))
    
    return answer.strip('.')