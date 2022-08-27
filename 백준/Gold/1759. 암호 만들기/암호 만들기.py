l,c = map(int,input().split())
alpha = list(input().split())
alpha.sort()

def bruteforce(st,cnt,idx):
    if cnt>=l:
        vowel_f = 0
        cnt = 0
        for ch in st:
            if ch in ['a','e','i','o','u']:
                vowel_f=1
            else:
                cnt += 1
        if vowel_f and cnt >=2:
            print(st)
        return
    for j in range(idx,c):
        bruteforce(st+alpha[j],cnt+1,j+1)

for i in range(c-l+1):
    bruteforce(alpha[i],1,i+1)