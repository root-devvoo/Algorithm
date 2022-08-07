X = int(input())
N = int(input())

result = 0

for _ in range(N):
    a, b = map(int, input().split())
    result += int(a*b)

# 최종 결과 출력
if result == X:
    print('Yes')
else:
    print('No')  
