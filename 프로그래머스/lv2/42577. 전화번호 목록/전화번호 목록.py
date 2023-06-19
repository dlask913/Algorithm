def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book,key = lambda x: (x,len(x)))
    for k,v in enumerate(phone_book[:-1]):
        if v == phone_book[k+1][:len(v)]:
            return False
    return answer