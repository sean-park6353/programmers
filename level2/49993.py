
def solution(a, arr):
    cnt=0
    for k in arr:
        answer=[]
        for i in k:
            if i in a:
                answer.append(i)
        result=''.join(answer)
        if len(a)==len(result):
            if a==result:
                cnt+=1

        else:
            tmp=0
            for i in range(len(result)):
                if result[i]==a[i]:
                    tmp+=1
            if tmp==len(result):
                cnt+=1
    return cnt


a="cbd"
arr=["bacde","cbadf","aecb","bda","cxpvd"]

print(solution(a,arr))
