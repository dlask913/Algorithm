from collections import Counter
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

print(int(round(sum(num)/n,0)))
num.sort()
print(num[n//2])
cnt = Counter(num).most_common()
if len(cnt)>1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(abs(num[0]-num[-1]))

