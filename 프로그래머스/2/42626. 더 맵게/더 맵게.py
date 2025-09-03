from heapq import *

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while len(scoville) != 1:
        first = heappop(scoville)
        if first >= K: return cnt
        second = heappop(scoville)
        heappush(scoville,first + (second * 2))
        cnt += 1
    if scoville[0] < K:
        return -1
    else: return cnt