def solution(lottos, win_nums):
    dic = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    cnt = lottos.count(0)
    res = set(lottos)&set(win_nums)
    answer=[]
    if not res:
        answer = [dic[cnt],6]
    else:
        answer = [dic[len(res)+cnt],dic[len(res)]]
    
    return answer