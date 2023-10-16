from itertools import product

def binary_search(l,r,score,arr): # score 이상 index 찾기
    while l < r:
        mid = (l+r)//2
        if arr[mid] < score:
            l = mid + 1
        else:
            r = mid
            
    if arr[r] < score:
        return len(arr)-r-1
    return len(arr)-r


def solution(info, query):
    answer = []
    info_dict = {}
    for i in product(['cpp', 'java', 'python', '-'], ['backend', 'frontend', '-'], ['junior', 'senior', '-'], ['chicken', 'pizza', '-']): # 가능한 모든 경우 
        info_dict[' '.join(i)] = []
    
    for i, inf in enumerate(info): # info 로 가능한 모든 경우
        lan, pos, exp, food, score = inf.split()
        score = int(score)
        for l, p, c, f in product([lan, '-'], [pos, '-'], [exp, '-'], [food, '-']):
            info_dict[' '.join([l, p, c, f])].append(score)
    
    for k in info_dict: # 점수대로 정렬
        info_dict[k].sort()
            
    for q in query:
        condition, score = q.rsplit(' ', 1)
        score = int(score)
        conditions = condition.split(" and ")
        t = info_dict[' '.join(conditions)]
        
        tmp = 0
        if t:
            tmp = binary_search(0,len(t)-1,score,t)
        answer.append(tmp)
        
    return answer