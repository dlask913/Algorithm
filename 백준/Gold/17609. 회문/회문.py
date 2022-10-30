t = int(input())
st = []
for _ in range(t):
    st.append(input())

def palindrome(x):
    if x == x[::-1]:
        return 0
    start = 0
    end = len(x) - 1
    l_flag = 0
    r_flag = 0
    while start<=end:
        if x[start]!=x[end]:
            if x[start+1]==x[end]:
                temp = x[start+1:end+1]
                if temp == temp[::-1]:
                    l_flag = 1
            if x[start]==x[end-1]:
                temp = x[start:end]
                if temp == temp[::-1]:
                    r_flag = 1
            if l_flag or r_flag: return 1
            else: return 2
        start += 1
        end -= 1

for i in st:
    print(palindrome(i))