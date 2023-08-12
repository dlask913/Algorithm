def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x :(x[col-1], -x[0]))
    xor = []
    for i in range(row_begin-1,row_end):
        s = 0
        for x in data[i]:
            s += (x%(i+1))
        xor.append(s)
        
    answer = xor[0]
    for x in xor[1:]:
        answer = answer^x
    
    return answer