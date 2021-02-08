from collections import OrderedDict

def solution(money):
    if not money:
        return 0
    if len(money)<=2:
        return max(money)
    dp=OrderedDict()
    dp[0],dp[1]=money[0],max(money[0],money[1])
    for i in range(2,len(money)):
        dp[i]=max(dp[i-1],dp[i-2]+money[i])
    return dp.popitem()[1]