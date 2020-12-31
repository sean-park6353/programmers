def solution(arr):
    tmp = arr[0]
    result = []
    if len(arr) == 1:
        return arr[0]
    if tmp == arr[1]:
        result.append(tmp)
    else:
        result.append(tmp)
    for i in range(1, len(arr)):
        if tmp == arr[i]:
            continue
        else:
            tmp = arr[i]
            result.append(arr[i])

    return result
