n = int(input())
lst = []
for i in range(n):
    num = int(input())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)
print(sum(lst))