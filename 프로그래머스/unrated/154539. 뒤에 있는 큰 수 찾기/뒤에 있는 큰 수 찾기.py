def solution(numbers):
    stack = []
    n = len(numbers)
    res = [-1 for _ in range(n)]

    stack.append(0)
    for i in range(1,n):
        if numbers[i] > numbers[stack[-1]]:
            while stack and numbers[stack[-1]] < numbers[i]: 
                res[stack.pop()] = numbers[i]
        stack.append(i)
    
    return res