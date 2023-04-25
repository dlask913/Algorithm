n = int(input())
pat = input().split('*')
res = []
for _ in range(n):
    st = input()
    if len(pat[0])+len(pat[1]) > len(st):
        res.append("NE")
        continue
    if pat[0] == st[:len(pat[0])] and pat[1] == st[-len(pat[1]):]:
        res.append("DA")
    else:
        res.append("NE")

for i in res:
    print(i)
