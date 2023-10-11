def solution(record):
    answer = []
    res = []
    dic = {} # userId 별로 닉네임 저장할 공간
    for i in record:
        tmp = i.split() # 명령, userId, nickname 순
        if tmp[0] == "Enter":
            dic[tmp[1]] = tmp[2]
            answer.append((tmp[1],tmp[0]))
        elif tmp[0] == "Leave":
            answer.append((tmp[1],tmp[0]))
        else:
            dic[tmp[1]] = tmp[2]
        
    for ans in answer:
        if ans[1] =="Enter":
            res.append(dic[ans[0]]+"님이 들어왔습니다.")
        else:
            res.append(dic[ans[0]]+"님이 나갔습니다.")
    
    return res