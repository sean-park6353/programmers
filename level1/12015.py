def solution(strings, n):
    strings.sort()
    tmp = sorted(strings, key=lambda x: x[n])
    return tmp


#! 숏코드
# def solution(strings, n):
#     return sorted(sorted(strings) ,key= lambda x: x[n])
