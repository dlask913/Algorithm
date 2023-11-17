from itertools import permutations
from collections import deque
import copy
def solution(expression):
    ans = []
    ops = []
    for i in ['-','+','*']: # 사용할 연산자 구하기
        if i in expression:
            ops += [i]

    items = []
    idx = 0
    for k,v in enumerate(expression): # 숫자와 연산자 구분하기
        if not v.isdigit():
            items.append(expression[idx:k])
            items.append(v)
            idx = k+1
    else:
        items.append(expression[idx:])
            
    for op in permutations(ops): # 연산자 조합 ex> (-,+,*)
        cur = deque(items)
        nex = deque()
        for o in op:
            while cur:
                x = cur.popleft()
                if nex and nex[-1] == o: # 이전 값이 계산할 연산자이면 앞 뒤 숫자로 계산한 결과 저장
                    mid = nex.pop()
                    y = nex.pop()
                    x = str(eval(y+mid+x))
                nex.append(x)
            cur = copy.deepcopy(nex) # 재계산
            nex.clear()
        
        ans.append(abs(int(cur.pop())))
        
    return max(ans)
