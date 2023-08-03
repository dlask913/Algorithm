import math
def solution(fees, records):
    result=[]
    dic = {}
    for i in records:
        i=list(i.split())
        if i[1] not in dic: dic[i[1]]=[i[0]]
        else: dic[i[1]].append(i[0])
    dic = dict(sorted(dic.items()))
    
    for i in dic.keys():
        t=0
        dic[i].append('')
        for j,k in zip(dic[i][0::2],dic[i][1::2]):
            in_h,in_m=map(int,j.split(':'))
            if k: out_h,out_m=map(int,k.split(':'))
            else: out_h,out_m=23,59
            t += (out_h*60+out_m)-(in_h*60+in_m)
        if t>fees[0]:
            c = fees[1]+math.ceil((t-fees[0])/fees[2])*fees[3]
        else:
            c = fees[1]
        result.append(c)
    return result