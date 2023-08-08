import copy
def solution(s):
    dic ={')':'(','}':'{',']':'['}
    answer = 0
    for _ in range(len(s)):
        s = s[1:]+s[0]
        tmp = copy.deepcopy(s)
        stack = []
        for x in tmp:
            if x=='(' or x=='[' or x=='{':
                stack.append(x)
            elif stack and dic[x]==stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        if not stack:
            answer += 1
    return answer