N = int(input())
member = []

# 2차원 리스트 형식으로 들어가게끔 데이터 받음
for _ in range(N):
    member.append(list(input().split()))

# 나이를 기준으로 정렬하기
member.sort(key=lambda a:int(a[0]))             

for i in range(N):
    print(member[i][0], member[i][1])
