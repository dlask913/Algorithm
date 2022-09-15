import math
st = input()

cnt = 0
for i in range(1,len(st)):
    if st[i-1] != st[i] :
        cnt += 1
print(math.ceil(cnt/2))