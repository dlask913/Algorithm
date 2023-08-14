from itertools import combinations
def solution(elements):
    ans = set(elements)
    n = len(elements)
    for i in range(n):
        s = elements[i]
        for j in range(i+1,i+n-1):
            s += elements[j%n]
            ans.add(s)
    ans.add(sum(elements))
    return len(ans)