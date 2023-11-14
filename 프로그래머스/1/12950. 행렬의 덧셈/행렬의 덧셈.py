def solution(arr1, arr2):
    n,m = len(arr1),len(arr1[0])
    answer = [[arr1[i][j]+arr2[i][j] for j in range(m)] for i in range(n)]
    return answer