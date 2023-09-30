from itertools import combinations
def prime_number(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
    
def solution(nums):
    answer = 0
    for i in list(combinations(nums,3)):
        if prime_number(sum(i)):
            answer += 1
    return answer