from collections import deque
def solution(skill, skill_trees):
    answer = 0
    l = len(skill)
    
    for tree in skill_trees:
        q = deque()
        for s in tree: # skill 에 해당하는 문자열 빼고 담기
            if s in skill:
                q.append(s)
    
        flag = True
        for i in range(len(q)):
            if q[i] != skill[i]: # skill 과 tree 를 순서대로 비교했을 때 다르면 False
                flag = False
        else:
            if flag:
                answer += 1
        
    return answer