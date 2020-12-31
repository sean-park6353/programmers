def solution(answers):
    a = [1, 2, 3, 4, 5]*len(answers)
    b = [2, 1, 2, 3, 2, 4, 2, 5]*len(answers)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers)
    x = 0
    y = 0
    z = 0
    for i in range(len(answers)):
        if i == len(answers):
            break
        if answers[i] == a[i]:
            x += 1
    for i in range(len(answers)):
        if i == len(answers):
            break
        if answers[i] == b[i]:
            y += 1
    for i in range(len(answers)):
        if i == len(answers):
            break
        if answers[i] == c[i]:
            z += 1
    arr = [x, y, z]
    if x == y == z:
        return [1, 2, 3]
    elif x == y == max(arr):
        return [1, 2]
    elif y == z == max(arr):
        return [2, 3]
    elif x == z == max(arr):
        return [1, 3]
    else:
        return [arr.index(max(arr))+1]


answers = [2, 1, 2, 3, 2, 1, 2, 3, 4, 5, 1, 2]
