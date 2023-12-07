def solution(sequence, k):
    res = []
    if k in sequence:
        return [sequence.index(k),sequence.index(k)]
    l,r=0,0
    s=0
    while r<len(sequence):
        s += sequence[r]
        if s > k:
            s -= sequence[l]
            l += 1
        if s == k:
            if not res or (res[1]-res[0]) > (r-l): 
                res=[l,r]
        if s > k:
            s -= sequence[r]
        else: 
            r += 1
    return res