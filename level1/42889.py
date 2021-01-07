def solution(N, stages):
    tuple_list = []
    answer = []
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
        tuple_list.append((i, rate))
    tuple_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
    for i in tuple_list:
        answer.append(i[0])
    return answer


# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
