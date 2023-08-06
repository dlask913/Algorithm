from collections import deque
def solution(topping):
    answer = 0
    dic = {i:0 for i in topping}
    for i in topping:
        dic[i]+=1
    
    left = topping
    right = set()
    while left:
        x = left.pop()
        dic[x] -= 1
        if dic[x] == 0:
            del dic[x]
        right.add(x)
        if len(dic) == len(right):
            answer += 1
    
    return answer