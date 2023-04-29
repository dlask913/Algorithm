n = int(input())
win = 0
one=[0]
two=[0]
end = 48*60
for _ in range(n):
    w,t = input().split()
    mm,ss=map(int,t.split(":"))
    time = mm*60 + ss

    if w == '1':
        if one[0] == two[0]:
            if len(one) == 1:
                one.append(end - time)
            else:
                one[1] += (end - time)
        one[0] += 1
        if one[0] == two[0]:
            two[1] -= (end-time)
    else:
        if one[0] == two[0]:
            if len(two) == 1:
                two.append(end - time)
            else:
                two[1] += (end - time)
        two[0] += 1
        if one[0] == two[0]:
            one[1] -= (end - time)

if len(one) == 1:
    print("00:00")
else:
    print('{:0>2}:{:0>2}'.format((one[1])//60, (one[1])%60))
if len(two) == 1:
    print("00:00")
else:
    print('{:0>2}:{:0>2}'.format((two[1])//60, (two[1])%60))