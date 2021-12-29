N, M = map(int, input().split()) # 입력 첫째 줄
cards = list(map(int, input().split())) # 입력 둘째 줄

total = 0    
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            if cards[i] + cards[j] + cards[k] > M: # 세 카드를 더한 값이 M보다 클(초과) 경우
                continue
            else: # 세 카드를 더한 값이 M보다 미만일 경우
                total = max(total, (cards[i] + cards[j] + cards[k]))
                # 정답의 가능성이 있으므로 total값과 비교해서 최대값 total에 덮어 저장

print(total)

'''
3중 for문을 쓰면 '시간 초과' 같은게 뜰 줄 알았는데, 맞았다! lol
다른 사람 풀이 중에서는 보다 효율적인 방법으로 푼 해답이 있을거라고 생각한다.
'''
