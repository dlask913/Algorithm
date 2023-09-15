from itertools import combinations
def solution(numbers):
    tmp = set(map(sum,combinations(numbers, 2)))
    answer = sorted(list(tmp))
    
    return answer