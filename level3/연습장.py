arr=[2,3,4,5,11,10]
start=0
end=4
target=13

answer=[]
while start!=end:
    if arr[start]+arr[end]>target:
        end-=1
    elif arr[start]+arr[end]<target:
        start+=1
    else:
        answer=[start,end]
        break
print(answer)