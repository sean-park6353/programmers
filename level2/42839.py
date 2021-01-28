from itertools import permutations

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def func1(t):
    tmp=[]
    for i in range(len(t)):
        tmp.append(t[i])
    return tmp
def solution(numbers):
    arr=list(map(int,numbers.strip()))
    answer=[]
    for i in range(1,len(numbers)+1):
        tmp=list(permutations(arr,i))
        for j in tmp:
            answer.append(j)
    answer=list(map(func1,answer))
    x=[]
    for i in answer:
        if i not in x:
            x.append(i)
    result=[]
    for number in x:
        value=""
        for j in number:
            value+=str(j)
        aim=int(value)
        if aim not in result:
            result.append(aim)
    answer=0
    for i in result:
        if is_prime(i):
            answer+=1
    return answer
solution("17")