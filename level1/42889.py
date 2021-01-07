def solution(N, stages):
    rateArr = []
    tmp = []
    l = []
    for i in range(1, N+1):
        challenger = 0
        complete = stages.count(i)
        for j in range(len(stages)):
            if stages[j] >= i:
                challenger += 1
        if challenger == 0:
            rate = 0
        else:
            rate = complete/challenger
        rateArr.append(rate)
        tmp.append(i)
    for i in range(N):
        l.append((tmp[i], rateArr[i]))
    answer = sorted(l, key=lambda x: x[1], reverse=True)
    q = []
    for i in answer:
        q.append(i[0])
    return q


print(solution(3, [1, 2]))
