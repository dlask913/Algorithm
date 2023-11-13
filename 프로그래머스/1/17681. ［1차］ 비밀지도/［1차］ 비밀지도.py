def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)] 
    binary = [0 for _ in range(n)]

    for x in range(n): # 둘 중에 하나만 벽이어도 벽 -> OR
        binary[x] = arr1[x] | arr2[x]
    
    for i in range(n):
        for j in range(n-1,-1,-1): 
            # 해당 값이 벽인지 아닌지 확인하기 -> AND
            answer[i] += '#' if binary[i] & (1<<j) else ' '

    return answer