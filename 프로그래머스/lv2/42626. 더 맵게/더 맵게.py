import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            ab = a + b * 2
            heapq.heappush(scoville, ab)
            answer += 1
        except:
            return -1
    return answer