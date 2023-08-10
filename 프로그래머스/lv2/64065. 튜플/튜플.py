def solution(s):
    dic = {}
    for i in s.split('},'):
        tmp = i.replace('{','')
        tmp = tmp.replace('}','')
        tmp = tmp.split(',')
        for x in tmp:
            if int(x) not in dic:
                dic[int(x)] = 1
            else:
                dic[int(x)] += 1
    arr = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    answer = [i[0] for i in arr]
    return answer