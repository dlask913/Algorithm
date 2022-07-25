s= int(input())
sum_ = 0
i = 0
while True:
    if s<=sum_:
        if s==sum_:
            print(i)
        else:
            print(i-1)
        break
    i+=1
    sum_ += i
