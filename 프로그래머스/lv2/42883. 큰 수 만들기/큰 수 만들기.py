
def solution(number, k):
    ans =''
    stack = []
    for i in number:
        while True:
            if stack and stack[-1]<i and k>0:
                stack.pop()
                k -=1
            else: break
        stack.append(i)
    if k != 0:
        stack = stack[:len(number)-k]
        
    return ''.join(stack)