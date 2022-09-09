def solution(participant, completion):
    ans={}
    for i in (participant+completion):
        if i not in ans:
            ans[i]=1
        else:
            ans[i]+=1
    for i in ans.keys():
        if ans[i] %2 != 0:
            return i