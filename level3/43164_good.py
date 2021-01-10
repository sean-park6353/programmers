import re
from collections import Counter
# import sys
# sys.setrecursionlimit(500000)


result = ""


def dfs(x, y, graph, visit, tickets, dict_my):
    global result
    start = dict_my[x]
    arrival = dict_my[y]
    visit[x][y] = 1
    if len(tickets) == 0:
        result += str((x, y))
        return result
    else:
        result += str((x, y))
        for i in range(len(graph[y])):
            if len(tickets) == 0:
                return result
            if graph[y][i] != 1:
                if i == len(graph[y]-1):
                    return
                continue
            if visit[y][i] != 0:
                for j in tickets:
                    start = dict_my[y]
                    arrival = dict_my[i]
                    if [start, arrival] == j:
                        tickets.remove([start, arrival])
                        dfs(y, i, graph, visit, tickets, dict_my)
                        break
                continue
            start = dict_my[y]
            arrival = dict_my[i]
            tickets.remove([start, arrival])
            dfs(y, i, graph, visit, tickets, dict_my)
    return result


def solution(tickets):
    tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    airport = []
    x = -1
    y = -1
    # for i in tickets:
    #     print(i)
    for i in range(len(tickets)):
        for j in range(len(tickets[i])):
            airport.append(tickets[i][j])
    airport_cnt = len(list(set(airport)))

    # print(airport_cnt)
    numarr = [i for i in range(len(list(set(airport))))]
    graph = [[0]*airport_cnt for i in range(airport_cnt)]
    my_dict = dict(zip(sorted(list(set(airport))), numarr))
    # print(my_dict)
    dict_my = {b: a for a, b in my_dict.items()}
    # print(dict_my)
    visit = [[0]*airport_cnt for i in range(airport_cnt)]
    for i in range(len(tickets)):
        graph[my_dict['%s' % tickets[i][0]]][my_dict['%s' % tickets[i][1]]] = 1
    # for i in graph:
    #     print(i)
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            (x, y) = (my_dict[tickets[i][0]], my_dict[tickets[i][1]])
            break
    # print(tickets)
    start = dict_my[x]
    arrival = dict_my[y]
    tickets.remove([start, arrival])
    # for i in tickets:
    #     print(i)
    answer = dfs(x, y, graph, visit, tickets, dict_my)
    answer = re.findall(r"[\d']+", "".join(answer))
    answer = list(map(int, answer))
    # return answer
    route = []
    for i in range(len(answer)):
        for m, n in my_dict.items():
            if answer[i] == n:
                route.append(m)
                break
    # return route
    new = [route[0]]
    for i in range(1, len(route)-1):
        if route[i] != route[i+1]:
            new.append(route[i])
    new.append(route[-1])
    # print(new)
    return new


# print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
#     "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
    # "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"], ["SFO", "ATL"], ["ATL", "ICN"]]))
# print(solution([["ICN", "SFO"], ["SFO", "ICN"],
#                 ["ICN", "SFO"], ["SFO", "ATL"], ["ATL", "SFO"]]))
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

# print(solution([["ICN", "ATL"], ["ICN", "BAR"], ["BAR", "ICN"]]))
