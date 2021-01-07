def func(number, n):
    binaryNum = bin(number)[2:]
    tmpArr = []
    if len(binaryNum) < n:
        for i in range(n-len(binaryNum)):
            tmpArr.append("0")
        for i in range(len(binaryNum)):
            tmpArr.append(binaryNum[i])
    else:
        for i in range(len(binaryNum)):
            tmpArr.append(binaryNum[i])
    graph = []
    for i in range(len(tmpArr)):
        for j in range(len(tmpArr[i])):
            if tmpArr[i][j] == "0":
                graph.append(" ")
            else:
                graph.append("#")
    return graph


def solution(n, arr1, arr2):
    newarr1 = []
    newarr2 = []
    strarry = [[' ']*n for i in range(n)]
    for i in range(len(arr1)):
        newarr1.append(func(arr1[i], n))
        newarr2.append(func(arr2[i], n))
    for i in range(n):
        for j in range(n):
            if newarr1[i][j] == ' ' and newarr2[i][j] == ' ':
                strarry[i][j] = ' '
            elif newarr1[i][j] == '#' or newarr2[i][j] == '#':
                strarry[i][j] = '#'
    answer = []
    for i in range(n):
        tmp = ""
        for j in range(n):
            tmp += strarry[i][j]
        answer.append(tmp)
    return answer


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
