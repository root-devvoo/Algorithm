# 동적계획법 Bottom up 방법으로 접근한 풀이
# Bottom up 방법이란? 작은 문제에서 큰 문제로 반복문 호출
# (Bottom Up 방법은 규칙에 따라 정답을 찾아나가는데 있어서 반복문을 활용한 방법)
#################################### 참고 ####################################
# Top Down 방법이란? 큰 문제에서 작은 문제로 재귀 호출
# (Top Down은 재귀함수를 호출하여 재귀함수 아래까지 조사하는 방법)
#############################################################################
import sys

n = int(sys.stdin.readline())

def fib(n):
    fibList = [0, 1]
    for i in range(2, n+1):
        fibList.append(fibList[i-2] + fibList[i-1])
    return fibList[-1]

print(fib(n))
