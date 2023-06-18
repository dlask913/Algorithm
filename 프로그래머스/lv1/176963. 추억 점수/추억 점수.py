def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        cnt = 0
        for j in range(len(name)):
            if name[j] in i:
                cnt += yearning[j]
        answer.append(cnt)
    
    return answer