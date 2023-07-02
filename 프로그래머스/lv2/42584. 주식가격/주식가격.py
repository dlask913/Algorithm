def solution(prices):
    answer = []
    stack = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[j]>=prices[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
            
    return answer+[0]