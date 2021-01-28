from collections import deque



def solution(bridge_length, weight, truck_weights):
    time=0
    truck_weights=deque(truck_weights)
    bridge= deque([0 for _ in range(bridge_length)])
    while len(bridge)!=0:
        time+=1
        bridge.popleft()
        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return time


print(solution(2,10,[7,4,5,6]))