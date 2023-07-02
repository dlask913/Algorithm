def solution(prices):
    answer = []
    stack = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt += 1
            if prices[j]<prices[i]:
                break
        answer.append(cnt)
            
    return answer+[0]