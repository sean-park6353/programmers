def func(left, right,s):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    return s[left+1:right]


def solution(s):
    if len(s)<2 or s==s[::-1]:
        return len(s)
    result=''
    for i in range(len(s)-1):
        result=max(result,func(i,i+1,s),func(i,i+2,s),key=len)
    return len(result)