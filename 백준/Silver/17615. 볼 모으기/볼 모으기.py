n = int(input())
ball=input()
cnt = [0 for _ in range(4)]
# 빨간색 공을 오른쪽으로 옮기는 경우
flag = 0
for i in range(n-1,-1,-1):
    if ball[i]=='B':
        flag = 1
    if flag and ball[i]=='R':
        cnt[0] += 1

# 빨간색 공을 왼쪽으로 옮기는 경우
flag =0
for i in range(n):
    if ball[i]=='B':
        flag=1
    if flag and ball[i]=='R':
        cnt[1]+=1

# 파란색 공을 오른쪽으로
flag = 0
for i in range(n-1,-1,-1):
    if ball[i] =='R':
        flag =1
    if flag and ball[i]=='B':
        cnt[2]+=1

#파란색 공을 왼쪽으로
flag = 0
for i in range(n):
    if ball[i] == 'R':
        flag=1
    if flag and ball[i]=='B':
        cnt[3]+=1

print(min(cnt))
