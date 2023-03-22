s = input()
res = ''
stack = ''
flag = False
for i in s:
    if i == '<':
        if stack:
            res += stack[::-1]
            stack= ''
        res += i
        flag = True
        continue
    elif flag:
        res+=i
        if i=='>':
            flag = False
        continue
    if not flag and i == ' ':
        if stack:
            res += ( stack[::-1] + ' ' )
            stack= ''
        continue
    stack += i
if stack:
    res += stack[::-1]
    stack= ''
print(res)
    
