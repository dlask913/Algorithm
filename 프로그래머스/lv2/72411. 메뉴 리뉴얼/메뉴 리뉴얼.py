from itertools import combinations
def solution(orders, course):
    answer = []
    dic = {}
    for c in course:
        tmp = []
        for i in orders: # orders 전체 문자열로 조합하면 시간초과
            for j in combinations(i,c):
                tmp.append(sorted(''.join(list(j))))
        
        m=2 # 최대 주문 수
        for i in tmp:
            cnt = 0
            for j in orders:
                if len(set(j) & set(i)) == len(i): # 해당 조합(i)이 있는 경우
                    cnt += 1
            if cnt>=m:
                m = m if m > cnt else cnt
                dic[''.join(list(i))] = cnt
                
        for k,v in dic.items():
            if v==m and i not in answer:
                answer.append(k)
        dic.clear()
        
    answer.sort()
    return answer