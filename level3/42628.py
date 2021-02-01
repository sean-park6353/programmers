from collections import deque
import heapq,copy
q=deque([])

def myfunc(num):
    if num<0:
        return -num
    else:
        return -num
def insert(q,num):
        # print("q에 num 추가")
        q.append(num)
def delete(tmp,num):
    global q
    if tmp:
        if num==1:
            arr=[]
            for i in range(len(tmp)):
                heapq.heappush(arr,-tmp[i])
            print(arr)
            arr=deque(map(myfunc,arr))
            print(arr)
            arr.popleft()
            q=copy.deepcopy(arr)
        else:
            z=list(tmp)
            heapq.heapify(z)
            z=deque(z)
            z.popleft()
            q=copy.deepcopy(z)
def solution(operations):
    for i in operations:
        op,num=map(str,i.split())
        num=int(num)
        if op=="I":
            insert(q,num)
        elif op=="D":
            delete(q,num)
    return [max(q),min(q)]
# operations=["I -45","I 653","D 1","I -642","I 45","I 97","D 1","D -1","I 333"]
print(solution(operations))