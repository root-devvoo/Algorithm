N = int(input())
bulk = []

# 각 사람의 몸무게와 키를 나타내는 양의 정수 x, y 입력 
for _ in range(N):
    x, y = map(int, input().split())
    bulk.append((x, y)) # 리스트에 튜플 형태로 저장

for i in bulk:
    rank = 1 # 기본 순위는 1위로 고정
    for j in bulk: 
        if i[0] < j[0] and i[1] < j[1]: # 각 사람들의 키와 몸무게를 일일히 비교해서
            rank += 1 # 자신보다 큰 덩치가 있다면 자신의 rank를 증가 시키도록 함
    print(rank, end = ' ') # 각 덩치 등수 공백문자로 분리시켜 출력
