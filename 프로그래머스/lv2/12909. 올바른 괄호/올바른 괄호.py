def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if not stack and i==')':
            answer = False
            break
        if i=='(': stack.append(i)
        else: stack.pop()
    if stack: answer = False
    
    return answer