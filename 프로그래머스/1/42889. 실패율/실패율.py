from collections import Counter
def solution(N, stages):
    answer = []
    pro = Counter(stages) # 스테이지별 실패 횟수
    stages.sort()
    l = len(stages) # 총 인원
    
    for x in range(1,N+1):
        if x in stages:
            idx = stages.index(x) # 가장 처음 index를 활용하여 총 인원 계산
            answer.append((pro[x]/(l-idx),x))
        else: 
            answer.append((0,x)) # 없으면 실패율 0
    answer.sort(key=lambda x:(-x[0], x[1]))
    
    return [x[1] for x in answer]