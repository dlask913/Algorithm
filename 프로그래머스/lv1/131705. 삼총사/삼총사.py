from itertools import combinations
def solution(number):
    answer = 0
    for x in combinations(number,3):
        if sum(x) == 0:
            answer += 1
    return answer