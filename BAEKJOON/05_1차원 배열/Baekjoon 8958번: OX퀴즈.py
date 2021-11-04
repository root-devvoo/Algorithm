#import sys
#input = sys.stdin.readline()

n = int(input())

for _ in range(n):
    OX = list(input())
    point = 0
    sum_point = 0
    for j in OX:
        if j == 'O':
            point += 1 # O면 점수 1점씩 증가
        else:
            point = 0 # X일 경우
        sum_point += point
    print(sum_point)
