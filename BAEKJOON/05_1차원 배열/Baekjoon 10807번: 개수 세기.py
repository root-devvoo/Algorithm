# 런타임 에러 난 코드 (개빡)
N = int(input())
numbers = []

for _ in range(N):
  numbers.append(int(input()))

v = int(input())
# 결과 출력
print(numbers.count(v))

### 코테 연습 및 공부에는 프로그래머스가 짱이다!

################ 정답 코드 ################
N = int(input())
numbers = list(map(int, input().split()))
v = int(input())
# 결과 출력
print(numbers.count(v))
###########################################
