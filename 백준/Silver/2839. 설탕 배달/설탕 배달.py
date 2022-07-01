n = int(input())
result = list()
idx = 0
for i in range(n):
    for j in range(n):
        if n == (5 * i + 3 * j):
            result.append(i + j)
            break
        if n < (5 * i + 3 * j):
            break
if not result:
    print("-1")
else:
    result.sort()
    print(result[0])