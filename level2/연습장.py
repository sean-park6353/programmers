# n=9
# arr=[0,12345678,1,2,0,0,0,0,32]
import heapq,sys
arr=[]
result=[]
heapq.heapify(result)
n=int(sys.stdin.readline())
for i in range(n):
    arr.append(int(sys.stdin.readline()))
for i in range(n):
    if arr[i]==0:
        if len(result)==0:
            print(0)
            continue
        else:
            print(heapq.heappop(result))   
    else:
        heapq.heappush(result,arr[i])