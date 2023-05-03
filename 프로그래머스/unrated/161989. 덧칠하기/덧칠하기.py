def solution(n, m, section):
    answer = 0
    idx = 0
    while idx<len(section):
        cur = section[idx]
        s = idx
        for i in range(s,len(section)):
            n = section[i]
            if n >= cur+m: break
            idx = i +1
        answer +=1
    return answer