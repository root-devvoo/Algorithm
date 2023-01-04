# 피보나치 수 구하는 함수
def fib(n):
    fibList = [0, 1]
    for i in range(2, n+1):
        fibList.append(fibList[i-2] + fibList[i-1])
    return fibList[-1]
# main
def solution(n):
    return fib(n) % 1234567
