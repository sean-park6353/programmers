
def solution(d):
    arr = []
    tmp = ""
    for i in d:
        if i.isnumeric():
            tmp += i
        elif i == "S":
            arr.append(int(tmp)**1)
            tmp = ""
        elif i == 'D':
            arr.append(int(tmp)**2)
            tmp = ""
        elif i == 'T':
            arr.append(int(tmp)**3)
            tmp = ""
        elif i == '*':
            if len(arr) == 1:
                arr[0] = arr[0]*2
            else:
                for j in range(2):
                    arr[-1-j] = arr[-1-j]*2
        elif i == '#':
            arr[-1] = arr[-1]*-1
    return sum(arr)


solution("1D2S3T*")
