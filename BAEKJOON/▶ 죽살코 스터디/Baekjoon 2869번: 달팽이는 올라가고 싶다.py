# 시간 초과 코드 1 (while문 써서) 
import sys

A, B, V = map(int, sys.stdin.readline().split())

snail = 0
day = 0

while snail < V:
    snail = snail + A
    snail = snail - B
    if snail == V:
        break
    elif snail > V:
        snail = snail + A
    day += 1

print(day)

# 시간 초과 코드 2 (이유를 모르겠다... sys import 하느라?)
import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
print(math.ceil((V-A) / (A-B)) + 1)

# 맞은 코드
import math

A, B, V = map(int, input().split())
print(math.ceil((V-A) / (A-B)) + 1)
############### 풀이 ###############
# 달팽이는 하루에 A-B만큼 올라간다
# 달팽이가 낮에 정상에 올라가면 더 이상 미끄러지지 않으므로
# 정상에서 A만큼 먼저 빼주고, 뺏던 하루를 더해줌
# 나눈 결과인 몫이 2.x, 3.x 와 같이 정수로 나누어 떨어지지 않는 경우가 있기 때문에
# math.ceil(x) 함수로 올림 하여 소수도 하루로 치도록 함
