

`dp=[0]*100


def func(n):
    if n==1 or n==2:
        return 1
    if dp[n]!=0:
        return dp[n]
    else:
        dp[n]=func(n-1)+func(n-2)
    return dp[n]`