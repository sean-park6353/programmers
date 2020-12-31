def solution(s):
    tmp = sorted(s, reverse=True)
    result = ""
    for i in tmp:
        result += i
    return result
