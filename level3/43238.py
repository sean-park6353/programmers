def solution(n,times):
    right=min(times)*2
    left=1
    answer=0
    while left<right:
        mid= (right+left)//2
        tmp=n
        for i in times:
            tmp-=mid//i
            if tmp<=0:
                answer=mid
                right=mid-1
                break
        if tmp>0:
            left=mid+1
    return answer

print(solution(6,[7,10]))