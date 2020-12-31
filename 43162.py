

def dfs(x, computers, visit):
    visit[x] = True
    for i in range(len(computers[x])):
        if visit[i] == False and computers[x][i] == 1:
            dfs(i, computers, visit)


def solution(n, computers):
    visit = [False for i in range(n)]
    answer = 0
    for i in range(n):
        if visit[i] == False:
            answer += 1
            dfs(i, computers, visit)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
