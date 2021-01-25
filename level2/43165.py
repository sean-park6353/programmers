
import random


def solution(numbers, target):
    tmp = [0 for i in range(len(numbers)*2)]
    for i in range(1, len(tmp), 2):
        try:
            tmp[i] = numbers[i/2]
        except:
            break

    print(tmp)


# solution([1, 1, 1, 1, 1], 3)
#     while True:
#         flg = random.randrange(1, 3)
#         if flg == 1:
#             op = '-'
#         else:
#             op = '+'
#         value = eval()
