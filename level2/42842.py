def solution(brown,yellow):
    arr=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            arr.append(i)
    for i in range(len(arr)):
        size=0
        p=arr[i]
        q=arr[-1-i]
        graph=[[0]*p for _ in range(q)]
        size=(q*2)+(p*2)+4
        if size==brown:
            break
    answer=[q+2,p+2]
    return answer

print(solution(10,2))