from collections import deque
def get_index(st): # u 가 균형잡힌 문자열이 되는 idx
    cnt = {"(":0, ")":0}
    for idx,s in enumerate(st):
        if idx>0 and cnt["("] == cnt[")"]:
            return idx
        cnt[s] += 1
    return len(st)
        
def check(st): # u 가 올바른 문자열인지 check
    st = deque(st)
    stack = []
    while st:
        x = st.popleft()
        if x=="(":
            stack.append(x)
        elif stack and x==")":
            stack.pop()
        else:
            return False
    return True

def replace(st):
    res = ''
    for s in st:
        if s == "(":
            res += ")"
        else:
            res += "("
    return res

def convert(u,v):  
    if u == "":
        return ""
    
    idx = get_index(v)
    if check(u):
        return u + convert(v[:idx],v[idx:])
    else:
        return "(" + convert(v[:idx],v[idx:]) + ")" + replace(u[1:-1])

def solution(p):
    answer = ''
    idx = get_index(p)
    return convert(p[:idx], p[idx:])