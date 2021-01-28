from collections import deque
# arr=[95,90,99,99,80,99]
# speed=[1,1,1,1,1,1]
# arr=[93,30,55]
# speed=[1,30,5]
arr= deque([40,93,30,55,60,65])
speed=deque([60,1,30,5,10,7])


def solution(arr,speed):
    q=deque([])
    for i in arr:
        q.append(i)
    i=0
    answer=[]
    while q:
        cnt=0
        while True:
            if len(q)==0:
                break
            if q[i]<100:
                break
            else:
                q.popleft()
                speed.popleft()
                arr.popleft()
                cnt+=1
        if cnt!=0:
            answer.append(cnt)
        for k in range(len(q)):
            q[k]=q[k]+speed[k]
    return answer


    
print(solution(arr,speed))

