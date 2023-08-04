def solution(storey):
    answer = 0
    num = list(map(int, str(storey)))[::-1]
    num += [0]
    for k in range(len(num)):
        if storey==0: break
        c = 10 ** k
        if num[k] > 5 or (num[k] == 5 and num[k + 1] >= 5):
            tmp = num[k]
            storey += (10 - tmp) * c
            answer += abs(10 - tmp)
        elif num[k] <= 5 or (num[k] == 5 and num[k + 1] < 5):
            storey -= abs(num[k] * c)
            answer += num[k]
        num = list(map(int, str(storey)))[::-1]
        num += [0]
    return answer