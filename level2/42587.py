from collections import deque
def solution(arr, user):
    index = [i for i in range(len(arr))]
    tmp = tuple(zip(arr, index))
    q = deque(tmp)
    answer = 0
    cnt = 0
    while True:
        big = max(q)[0]
        if q[0][0] == big:
            answer, bread = q.popleft()
            if answer == arr[user] and bread == user:
                cnt += 1
                break
            cnt += 1
        else:
            q.append(q.popleft())
    print(15)
    print(34)
    return cnt