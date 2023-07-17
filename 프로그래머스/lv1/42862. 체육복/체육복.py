def solution(n, lost, reserve):
    borr = set()
    reserve = set(reserve)
    lost.sort()
    for l in lost:
        if l in reserve:
            borr.add(l)
        elif (l-1 in reserve) and (l-1 not in borr):
            borr.add(l-1)
        elif (l+1 in reserve) and (l+1 not in borr):
            borr.add(l+1)
            
    return n - len(lost) + len(borr)