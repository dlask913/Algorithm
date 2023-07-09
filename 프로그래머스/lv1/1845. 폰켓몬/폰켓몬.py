def solution(nums):
    answer = 0
    l = len(nums)//2
    nums = set(nums)
    
    if l >= len(nums):
        answer = len(nums)
    else:
        answer = l
    
    return answer