def func(word):
    new = ""
    for i in range(len(word)):
        if i % 2 == 0:
            new += word[i].upper()
        else:
            new += word[i].lower()
    return new


def solution(s):
    arr = s.split(" ")
    tmp = list(map(func, arr))
    return " ".join(tmp)


print(solution("l l l "))
