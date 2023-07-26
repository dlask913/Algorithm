def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-10+1):
        v = [0 for _ in range(len(want))]
        for j in range(len(want)):
            if discount[i:i+10].count(want[j])>=number[j]:
                v[j] = 1
        if all(v):
            answer += 1
    return answer