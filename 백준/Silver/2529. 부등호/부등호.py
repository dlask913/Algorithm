k = int(input())
sig = list(input().split())
res = []
def bruteforce(x,v,seq,tmp):
    if seq == k:
        res.append(''.join(map(str,tmp)))
        return
    if sig[seq] == ">":
        for i in range(x-1,-1,-1):
            if v[i] == 0:
                v[i] = 1
                bruteforce(i,v,seq+1,tmp+[i])
                v[i] = 0
    if sig[seq] == "<":
        for i in range(x+1,10):
            if v[i] == 0:
                v[i] = 1
                bruteforce(i,v,seq+1,tmp+[i])
                v[i] = 0

for i in range(10):
    v = [0 for _ in range(10)]
    v[i] = 1
    bruteforce(i,v,0,[i])
res.sort()
print(res[-1])
print(res[0])