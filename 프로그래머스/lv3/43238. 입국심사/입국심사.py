def solution(n, times):
    times.sort()
    start = 0
    answer = []
    end = n*times[-1]
    while start<=end:
        mid = (start+end) // 2
        tmp = 0
        for i in times:
            tmp += mid//i
        if tmp<n:
            start = mid + 1
        else:
            answer.append(mid)
            end = mid - 1

    return min(answer)