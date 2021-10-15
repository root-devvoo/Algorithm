n = int(input())
scores = list(map(int, input().split()))

M = max(scores)    
new_scores = []

# 모든 기존 점수를 점수/M*100으로 고쳐서 새로운 점수 리스트에 추가
for i in range(len(scores)):
    new_scores.append(scores[i] / M * 100)

print(sum(new_scores)/len(new_scores)) # 평균 계산
