st = input()
st = sorted(st)
flag = False
flag_r = False
tmp = ''
ans =''
i = 0
while i<=len(st)-1:
    if st.count(st[i])%2 != 0:
        if flag and tmp != st[i]:
            flag_r = True
            break
        flag = True
        tmp = st[i]
    if i < len(st)-1 and st[i] == st[i+1]:
        ans += st[i]
        i += 2
    else:
        i+=1

if flag_r:
    print("I'm Sorry Hansoo")
else:
    print(ans+tmp+ans[::-1])


