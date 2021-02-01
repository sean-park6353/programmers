import sys
n=int(sys.stdin.readline())
arr=[]
dpa=[1,0]
dpb=[0,1]
for i in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        print(1,0)
        continue
    for i in range(2,a+1):
        dpa.append(dpa[i-2]+dpa[i-1])
    for i in range(2,a+1):
        dpb.append(dpb[i-2]+dpb[i-1])
    print(dpa[-1],dpb[-1])

