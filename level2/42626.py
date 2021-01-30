import heapq
def solution(scoville,K):
    cnt=0
    heapq.heapify(scoville)
    while scoville:
        if K<=scoville[0]:
            break
        one=heapq.heappop(scoville)
        if len(scoville)==0:
            return -1
        two=heapq.heappop(scoville)
        cnt+=1
        target=one+(two*2)
        heapq.heappush(scoville,target)
        if K<=scoville[0]:
            break
    return cnt