import heapq

def solution(scoville, K):
    result = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2) # heappop은 heap 안에서 가장 적은 요소를 pop해줌
        heapq.heappush(scoville, mix)
        result += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return result
