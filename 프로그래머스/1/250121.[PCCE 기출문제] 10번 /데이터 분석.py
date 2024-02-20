def solution(data, ext, val_ext, sort_by):
    answer = []
    idx = {"code":0, "date":1, "maximum":2, "remain":3} # ext 에 해당하는 data index
    
    for x in data:
        if x[idx[ext]] < val_ext: # ext 에 해당하는 data value < 기준값
            answer.append(x)
    
    answer.sort(key=lambda x:x[idx[sort_by]]) # sort_by 기준 오름차순
    return answer
