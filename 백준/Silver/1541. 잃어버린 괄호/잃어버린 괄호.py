exp = input().split('-')
sum_ = 0
plus = exp[0]
minus = exp[1:]
if plus.isnumeric() or '+' in plus:
    sum_ += sum(list(map(int,plus.split('+'))))
if minus:
    for i in minus:
        sum_ -= sum(list(map(int,i.split('+'))))
print(sum_)