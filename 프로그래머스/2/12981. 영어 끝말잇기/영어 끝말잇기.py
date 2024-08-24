from collections import deque

def solution(n, words):
    answer = [0, 0]
    words = deque(words)
    stack = [words.popleft()]
    
    while words:
        if stack[-1][-1] != words[0][0] or words[0] in stack:
            answer = [len(stack)%n+1, len(stack)//n+1]
            break
        stack.append(words.popleft())
    
    return answer