def solution(order):
    answer = 0
    sub = []
    idx = 0
    
    for i in range(1,len(order)+1):
        sub.append(i)
        while idx<len(order) and sub:
            if sub[-1] == order[idx]:
                sub.pop()
                idx += 1
                answer += 1
            else:
                break
    
    return answer