st = input()
lst = []

for i in range(len(st)):
    lst.append(st[i:])
lst.sort()

for i in lst:
    print(i)