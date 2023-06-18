def solution(plans):
    answer = []
    for i in range(len(plans)):
        hh,mm = map(int,plans[i][1].split(':'))
        plans[i][1] = hh*60+mm
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x:x[1])
    stack = []
    stack.append(plans.pop(0))
    cur = stack[0][1]
    while stack:
        if not plans: 
            answer.append(stack[-1][0])
            stack.pop()
            continue
        n,s,p = plans.pop(0)
        while stack:
            if (cur+stack[-1][2]) <= s:
                cur += stack[-1][2]
                answer.append(stack[-1][0])
                stack.pop()
            else:
                stack[-1][2] -= (s-cur)
                break
        cur = s
        stack.append([n,s,p])
        
    return answer