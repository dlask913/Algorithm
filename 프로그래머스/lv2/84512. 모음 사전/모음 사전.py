res = 0
cnt = 0
def bruteforce(a, word, step, st):
    global res,cnt
    if st == word:
        res = cnt
    if step>=5: return
    for i in a:
        st += i
        cnt += 1
        bruteforce(a,word,step+1,st)
        st = st[:-1]
    
def solution(word):
    alpha = ['A','E','I','O','U']
    bruteforce(alpha,word,0,'')
    return res