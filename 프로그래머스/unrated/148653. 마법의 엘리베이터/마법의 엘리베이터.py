def solution(storey):
    answer = 0
    num = list(map(int, str(storey)))[::-1]
    num += [0]
    for k in range(len(num)):
        if storey==0: break
        c = 10 ** k
        if num[k] > 5 or (num[k] == 5 and num[k + 1] >= 5):
            storey += (10 - num[k]) * c
            answer += (10 - num[k])
        elif num[k] <= 5 or (num[k] == 5 and num[k + 1] < 5):
            storey -= (num[k] * c)
            answer += num[k]
        num = list(map(int, str(storey)))[::-1]
        num += [0]
    return answer