from collections import deque
def solution(s):
    answer = -1
    stack = []
    s = deque(s)
    stack.append(s.popleft())
    
    while s:
        x = s.popleft()
        if stack and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
            
    return 0 if stack else 1