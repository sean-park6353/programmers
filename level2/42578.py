from collections import Counter
from functools import reduce
clothes=[

    ["y","head"],
    ["b","eye"],
    ["g","head"],
    ["p","foot"]
    

]


def solution(clothes):
    cnt = Counter([types for name, types in clothes])
    result=[]
    answer=1
    for i in cnt.values():
        result.append(i+1)
    for i in result:
        answer*=i
    return answer-1




print(solution(clothes))
