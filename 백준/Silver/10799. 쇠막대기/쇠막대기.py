st = input()
stack = []
cnt = 0
for i in range(len(st)):
    if st[i] =="(":
        if st[i+1] ==")":
            cnt += len(stack)
        else:
            stack.append(st[i])
    elif st[i] ==")":
        if st[i-1] =="(":
            continue
        else:
            stack.pop()
            cnt += 1
print(cnt)
