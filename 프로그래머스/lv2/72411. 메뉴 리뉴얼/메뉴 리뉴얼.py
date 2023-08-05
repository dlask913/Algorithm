from itertools import combinations
def solution(orders, course):
    answer = []
    dic = {}
    for c in course:
        m = 2
        tmp = []
        for i in orders:
            for j in combinations(i,c):
                tmp.append(sorted(''.join(list(j))))
        
        for i in tmp:
            cnt = 0
            for j in orders:
                if len(set(j) & set(i)) == len(i):
                    cnt += 1
            if cnt>=m:
                m = m if m > cnt else cnt
                dic[''.join(list(i))] = cnt
        for k,v in dic.items():
            if k!=''.join(i) and len(set(k) & set(i)) == len(i) and v==m:
                continue
            if v==m and i not in answer:
                answer.append(k)
        dic.clear()
    answer.sort()
    return answer