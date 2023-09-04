from collections import deque
def solution(ingredient):
    # 1 빵, 2 야채, 3 고기 -> 1-2-3-1
    ingre = deque(ingredient)
    answer = 0
    q = []
    while ingre:
        q.append(ingre.popleft())
        if q[-4:]==[1,2,3,1]:
            for _ in range(4):
                q.pop()
            answer += 1
    return answer