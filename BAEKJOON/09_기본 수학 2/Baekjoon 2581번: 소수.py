# 소수 구하는 함수 정의
def isPrime(n):
    if(n<2):
        return False
    for i in range(2, n):
        if(n%i == 0):
            return False
    return True
  
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
M = int(input())
N = int(input())
answer = [] # 정답을 출력할 리스트 정의
# 입력한 숫자의 범위 내 반복
for x in range(M, N+1):
    if(isPrime(x)):
        # 소수이면 answer 리스트에 추가
        answer.append(x)
# 조건에 따라 결과 출력
if len(answer) == 0: # 소수가 없는 경우
    print(-1)
else:            
    print(sum(answer))
    print(min(answer))
