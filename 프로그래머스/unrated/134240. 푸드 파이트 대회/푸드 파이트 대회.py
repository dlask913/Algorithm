def solution(food):
    answer = ''
    tmp = ''
    for i in range(1,len(food)):
        tmp += str(i)*(food[i]//2)
    answer = tmp+'0'+tmp[::-1]
    return answer