def solution(players, callings):
    name_dic = {i:name for i,name in enumerate(players)}
    idx_dic =  {name:i for i,name in enumerate(players)}
    
    for i in callings:
        idx = idx_dic[i] # 해당 플레이어의 위치
        cur_n = name_dic[idx-1]
        name_dic[idx-1], name_dic[idx] = name_dic[idx],name_dic[idx-1]
        idx_dic[cur_n], idx_dic[i] = idx_dic[i],idx_dic[cur_n]
    
    answer = []
    for i in name_dic.values():
        answer.append(i)
        
    return answer