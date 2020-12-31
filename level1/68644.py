from itertools import combinations


def solution(numbers):
    answer = []
    a = list(combinations(numbers, 2))
    for i in a:
        answer.append(sum(i))
    a = list(set(answer))
    a.sort()
    print("성공")
    return a
