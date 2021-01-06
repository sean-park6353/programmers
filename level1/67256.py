

def func(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2)+abs(y1-y2)


def solution(numbers, hand):
    lpos = (3, 0)
    rpos = (3, 2)
    answer = ''
    for i in numbers:
        if i == 1:
            lpos = (0, 0)
            answer += 'L'
        elif i == 4:
            lpos = (1, 0)
            answer += 'L'
        elif i == 7:
            lpos = (2, 0)
            answer += 'L'
        elif i == 3:
            rpos = (0, 2)
            answer += 'R'
        elif i == 6:
            rpos = (1, 2)
            answer += 'R'
        elif i == 9:
            rpos = (2, 2)
            answer += 'R'
        elif i == 2:
            if func(rpos, (0, 1)) > func(lpos, (0, 1)):
                lpos = (0, 1)
                answer += "L"
            elif func(rpos, (0, 1)) < func(lpos, (0, 1)):
                rpos = (0, 1)
                answer += "R"
            else:
                if hand == "right":
                    rpos = (0, 1)
                    answer += "R"
                else:
                    lpos = (0, 1)
                    answer += "L"
        elif i == 5:
            if func(rpos, (1, 1)) > func(lpos, (1, 1)):
                lpos = (1, 1)
                answer += "L"
            elif func(rpos, (1, 1)) < func(lpos, (1, 1)):
                rpos = (1, 1)
                answer += "R"
            else:
                if hand == "right":
                    rpos = (1, 1)
                    answer += "R"
                else:
                    lpos = (1, 1)
                    answer += "L"
        elif i == 8:
            if func(rpos, (2, 1)) > func(lpos, (2, 1)):
                lpos = (2, 1)
                answer += "L"
            elif func(rpos, (2, 1)) < func(lpos, (2, 1)):
                rpos = (2, 1)
                answer += "R"
            else:
                if hand == "right":
                    rpos = (2, 1)
                    answer += "R"
                else:
                    lpos = (2, 1)
                    answer += "L"
        elif i == 0:
            if func(rpos, (3, 1)) > func(lpos, (3, 1)):
                lpos = (3, 1)
                answer += "L"
            elif func(rpos, (3, 1)) < func(lpos, (3, 1)):
                rpos = (3, 1)
                answer += "R"
            else:
                if hand == "right":
                    rpos = (3, 1)
                    answer += "R"
                else:
                    lpos = (3, 1)
                    answer += "L"

    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
