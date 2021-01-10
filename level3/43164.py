def solution(tickets):
    tickets.sort(reverse=True)
    print(tickets)
    routes = dict()
    for start, arrival in tickets:
        if start in routes:
            routes[start].append(arrival)
        else:
            routes[start] = [arrival]
    st = ['ICN']
    answer = []
    while st:
        top = st[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(routes[top].pop())
    answer.reverse()
    return answer
