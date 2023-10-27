def solution(x):
    st = list(str(x)) # 문자열 자릿수 저장
    num = sum(list(map(int,st))) # 정수로 형변환하여 합계 저장 
    return True if x%num == 0 else False