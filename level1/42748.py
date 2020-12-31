def func(n):
    return n-1


def solution(arr, commands):
    result = []
    for i in range(len(commands)):
        x, y, z = map(func, commands[i])
        brr = arr[x:y+1]
        brr.sort()
        result.append(brr[z])
    return result
