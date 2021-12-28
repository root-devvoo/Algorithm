# (소수 :: 1과 그 수 자신 이외의 자연수로는 나눌 수 없는 자연수이다.)
# 소수인지 검사하는 함수 정의 (에라토스테네스의 체 아님...)
def isPrime(n):
    if(n<2):
        return False
    for i in range(2, n):
        if(n%i == 0):
            return False
    return True

input() # 첫 줄에 수의 개수 N 입력받음
answer = 0
for n in map(int, input().split()): # N개의 수 입력받음
    if(isPrime(n)):
        answer += 1 # 소수이면 answer 변수에 1 더해 올려주기
print(answer)
