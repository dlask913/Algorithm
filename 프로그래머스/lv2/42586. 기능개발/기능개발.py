import math
def solution(progresses, speeds):
    answer = []
    stack = []
    for k,v in enumerate(progresses):
        stack.append(int(math.ceil((100-v)/speeds[k])))
    tmp = stack[0]
    idx,cnt = 1,1
    while idx<len(stack):
        if tmp < stack[idx]:
            answer.append(cnt)
            cnt = 0
            tmp = stack[idx]
        cnt += 1
        idx += 1
    answer.append(cnt)
    return answer