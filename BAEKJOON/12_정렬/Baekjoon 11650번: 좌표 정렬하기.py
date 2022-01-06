N = int(input())
locations = [] # 좌표들 리스트

# 좌표 입력 및 추가
for _ in range(N):
    x, y = map(int, input().split())
    locations.append((x, y)) # 좌표 값을 tuple 형태로 리스트에 저장

# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
locations.sort(key=lambda a: (a[0], a[1]))

for l in locations:
    print(l[0], l[1])
