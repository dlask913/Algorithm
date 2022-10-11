s = input()
sub = []
for i in range(1,len(s)+1):
    for j in range(len(s)):
        sub.append(s[j:j+i:])
print(len(set(sub)))