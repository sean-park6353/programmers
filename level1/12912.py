def solution(a, b):
    if a > b:
        answer = 0
        for i in range(b, a+1):
            answer += i
    else:
        answer = 0
        for i in range(a, b+1):
            answer += i

    return answer
