N = int(input())
locations = [] # 좌표들 리스트

# 좌표 입력 및 추가
for _ in range(N):
    x, y = map(int, input().split())
    locations.append((x, y))

# 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력
locations.sort(key=lambda a: (a[1], a[0]))

for l in locations:
    print(l[0], l[1])
