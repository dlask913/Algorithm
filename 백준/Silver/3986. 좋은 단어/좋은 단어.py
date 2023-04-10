n = int(input())
str = []
cnt = 0
for _ in range(n):
    str.append(input().strip())

for i in str:
    if i.count('A')%2 != 0 or i.count('B')%2 != 0:
        continue
    i = list(i)
    stack = []
    while i:
        tmp = i.pop()
        if stack and stack[-1] == tmp:
            stack.pop()
        else:
            stack.append(tmp)
    if not stack:
        cnt += 1
print(cnt)